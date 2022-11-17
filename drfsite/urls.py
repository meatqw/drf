
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from cats.views import *


# class MyCustomRouter(routers.SimpleRouter):
#     routes = [
#         routers.Route(url=r'^{prefix}$',
#                       mapping={'get': 'list'},
#                       name='{basename}-list',
#                       detail=False,
#                       initkwargs={'suffix': 'List'}),
#         routers.Route(
#             url=r'^{prefix}/{lookup}$',
#             mapping={'get': 'retrieve'},
#             name='{basename}-detail',
#             detail=True,
#             initkwargs={'suffix': 'Detail'}
#         ),

#     ]


router = routers.DefaultRouter()
router.register(r'cat', CatViewSet, basename='cat')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    # path('api/v1/catlist', CatAPIView.as_view()),
    # path('api/v1/catlist/', CatViewSet.as_view({'get': 'list'})),
    # path('api/v1/catlist/<int:pk>/', CatAPIView.as_view()),
    # path('api/v1/catlist/<int:pk>/', CatViewSet.as_view({'put': 'update'})),
    # path('api/v1/catdetail/<int:pk>/', CatAPIDetailView.as_view()),


]