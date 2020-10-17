from django.views.generic import CreateView
from apps.tickets.models import Ticket


class TicketCreateView(CreateView):

    template_name = 'tickets/add.html'
    model = Ticket
    fields = ('name', 'owner', "debtor", 'amount')
