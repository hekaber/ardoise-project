from django.shortcuts import render
from rest_framework import serializers, generics, permissions, status, views
from rest_framework.response import Response

# Create your views here.

class LoggedView(generics.GenericAPIView):

    def get(self, request):
        response = { 'message': 'hello' }
        return Response(response)
