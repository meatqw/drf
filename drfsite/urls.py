
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView, TokenObtainPairView
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


# router = routers.DefaultRouter()
# router.register(r'cat', CatViewSet, basename='cat')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/', include(router.urls)),

    path('api/v1/drf-auth/', include('rest_framework.urls')), # session auth

    path('api/v1/cat/', CatAPIList.as_view()),
    path('api/v1/cat/<int:pk>/', CatAPIUpdate.as_view()),
    path('api/v1/catdelete/<int:pk>/', CatAPIDestroy.as_view()),

    # path('api/v1/catlist/', CatViewSet.as_view({'get': 'list'})),
    # path('api/v1/catlist/<int:pk>/', CatAPIView.as_view()),
    # path('api/v1/catlist/<int:pk>/', CatViewSet.as_view({'put': 'update'})),
    # path('api/v1/catdetail/<int:pk>/', CatAPIDetailView.as_view()),

    # token auth
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # /auth/token/login

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),



]
