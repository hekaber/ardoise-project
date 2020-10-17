from django.shortcuts import render
from rest_framework import serializers, generics, permissions, status, views
from rest_framework.response import Response


class LoggedView(generics.GenericAPIView):

    def get(self, request):
        response = {'message': 'hello', 'request': request.GET}
        return Response(response)
