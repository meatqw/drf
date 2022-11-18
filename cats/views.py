from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms import model_to_dict
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .permissions import IsAdminReadOnly, IsOwnerOrReadOnly
from .models import Cat, Breed
from .serializers import CatSerializer


# class CatViewSet(viewsets.ModelViewSet):
#     """
#     CRUD
#     """
#     # queryset = Cat.objects.all()
#     serializer_class = CatSerializer


#     def get_queryset(self):
#         pk = self.kwargs.get('pk')

#         if not pk:
#             return Cat.objects.all()[:3]
#         else:
#             return Cat.objects.filter(pk=pk)

#     # new routes
#     @action(methods=['get'], detail=True)
#     def breed(self, request, pk=None):
#         breeds = Breed.objects.get(pk=pk)
#         return Response({"breeds": breeds.name})


# class CatViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.ListModelMixin,
#                    viewsets.GenericViewSet):
#     """
#     CRU (delete not allowed)
#     """
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer


# class CatViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     Only read
#     """
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer

class CatAPIListPagination(PageNumberPagination):
    """
    CUSTOM PAGINSTION
    """
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class CatAPIList(generics.ListCreateAPIView):
    """
    GET and POST request
    """
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = CatAPIListPagination


class CatAPIUpdate(generics.RetrieveUpdateAPIView):
    """
    UPDATE request
    """
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = (IsAuthenticated,)  # only auth user
    authentication_classes = (TokenAuthentication, )  # access only token


class CatAPIDestroy(generics.RetrieveDestroyAPIView):
    """
    DELETE request
    """
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = (IsAdminReadOnly,)

# class CatAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     """
#     CRUD request
#     """
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer

# class CatAPIView(APIView):
#     def get(self, request):
#         cat = Cat.objects.all()
#         return Response({'posts': CatSerializer(cat, many=True).data})

#     def post(self, request):
#         serializer = CatSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({'post': serializer.data})

#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({'error': "method put not allowed"})


#         try:
#             instance = Cat.objects.get(pk=pk)
#         except:
#             return Response({'error': "Object does not exist"})

#         serializer = CatSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({'post': serializer.data})

#     def delete(self, request, *args, **kwargs):

#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({'error': "method delete not allowed"})

#         try:
#             instance = Cat.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({'error': "Object does not exist"})


#         return Response({'post': 'delete post ' + str(pk)})


# Create your views here.
# class CatAPIView(generics.ListAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer
