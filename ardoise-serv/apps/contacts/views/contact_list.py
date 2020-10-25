from apps.contacts.models import Contact
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class ContactListView(LoginRequiredMixin, generic.ListView):

    login_url = '/accounts/login/'
    model = Contact
    context_object_name = 'contact_list'
    template_name = 'contacts/list.html'

    def get_queryset(self):

        search = self.request.GET.get('search', None)

        if search:
            return Contact.objects.get(pk=self.request.user.contact_id).contacts.filter(email__contains=search)
        return Contact.objects.get(pk=self.request.user.contact_id).contacts.all()
