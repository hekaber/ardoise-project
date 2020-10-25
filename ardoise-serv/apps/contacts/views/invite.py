from apps.contacts.models import Contact
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class InviteView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    model = Contact
    context_object_name = 'contact_list'
    template_name = 'contacts/invite.html'

    # def get_queryset(self):
    #
    #     return Contact.objects.all()
