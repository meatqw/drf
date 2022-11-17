from email.policy import default
import io

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Cat


# class CatModel:
#     def __init__(self, name, content):
#         self.name = name
#         self.content = content


class CatSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Cat
        fields = ("name", "content", "breed", "user")
        # fields = "__all__"
        
        
    # name = serializers.CharField(max_length=40)
    # content = serializers.CharField()
    # time_create = serializers.DateTimeField(read_only=True)
    # time_update = serializers.DateTimeField(read_only=True)
    # is_published = serializers.BooleanField(default=True)
    # breed_id = serializers.IntegerField()
    
    # def create(self, validated_data):
    #     return Cat.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.content = validated_data.get("content", instance.content)
    #     instance.time_update = validated_data.get("time_update", instance.time_update)
    #     instance.is_published = validated_data.get("is_published", instance.is_published)
    #     instance.breed_id = validated_data.get("breed_id", instance.breed_id)
    #     instance.save()
    #     return instance
        


# def encode():
#     model = CatModel('Cat', 'cat')
#     model_sr = CatSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json, sep='\n')


# def decode():
#     stream = io.BytesIO(b'{"name":"cat", "content":"content"}')
#     data = JSONParser().parse(stream)
#     serializer = CatSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
