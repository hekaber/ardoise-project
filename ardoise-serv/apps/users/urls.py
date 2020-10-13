from django.urls import path, include
from rest_framework import routers
from .views.user import UserViewSet
from .views.group import GroupViewSet


router = routers.DefaultRouter()
router.register(r'users_list', UserViewSet)
router.register(r'groups_list', GroupViewSet)

urlpatterns = [
    path('', include(router.urls))
]
