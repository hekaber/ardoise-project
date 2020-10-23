from django.shortcuts import render
from django.views.generic import View
from apps.tickets.forms import TicketForm
from apps.tickets.models import Ticket


class TicketCreateView(View):

    def get(self, request, *args, **kwargs):

        form = TicketForm(contact_id=request.user.contact_id)
        return render(request, 'tickets/add.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = TicketForm(request.POST, contact_id=request.user.contact_id)
        if form.is_valid():
            ticket = Ticket()
            ticket.name = form.cleaned_data['name']
            ticket.owner_id = form.cleaned_data['owner']
            ticket.debtor_id = form.cleaned_data['debtor']
            ticket.amount = form.cleaned_data['amount']
            ticket.currency_id = form.cleaned_data['currency']
            ticket.save()

        return render(request, 'tickets/add.html', {'form': form})
