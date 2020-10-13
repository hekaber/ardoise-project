from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from apps.users.serializers import UserSerializer, GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
