from tickets.models import Ticket
from tickets.serializers import TicketSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TicketList(APIView):

    def get(self, request, format=None):

        tickets = Tickets.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)
    
    
