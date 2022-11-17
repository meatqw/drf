from django.db import models

class Cat(models.Model):
    name = models.CharField(max_length=40)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    breed = models.ForeignKey('Breed', on_delete=models.PROTECT, null=True)


    def __str__(self):
        return self.name


class Breed(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name