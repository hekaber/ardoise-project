from apps.tickets.models import Ticket
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class TicketListView(LoginRequiredMixin, generic.ListView):

    login_url = '/accounts/login/'
    model = Ticket
    context_object_name = 'ticket_list'
    template_name = 'tickets/list.html'

    def get_queryset(self):

        return Ticket.objects.filter(owner__id=self.request.user.contact_id)
