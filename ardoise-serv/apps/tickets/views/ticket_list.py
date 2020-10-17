from apps.tickets.models import Ticket
from apps.tickets.serializers import Ticket

from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView


class TicketListView(APIView):

    def get(self, request, format=None):

        tickets = Ticket.objects.all()
        serializer = Ticket(tickets, many=True)
        return Response(serializer.data)


class TicketListTemplateView(TemplateView):

    template_name = 'tickets/list.html'
