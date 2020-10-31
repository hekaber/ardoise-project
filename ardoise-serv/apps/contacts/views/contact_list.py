from apps.contacts.models import Contact, Invite
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class ContactFriendsListView(LoginRequiredMixin, generic.ListView):

    login_url = '/accounts/login/'
    model = Contact
    context_object_name = 'contact_list'
    template_name = 'contacts/friends_list.html'

    def get_queryset(self):

        search = self.request.GET.get('search', None)

        if search:
            return Contact.objects.get(pk=self.request.user.contact_id).contacts.filter(email__contains=search)
        return Contact.objects.get(pk=self.request.user.contact_id).contacts.all()


class ContactListView(LoginRequiredMixin, generic.TemplateView):

    login_url = '/accounts/login/'
    model = Contact
    context_object_name = 'contact_list'
    template_name = 'contacts/invite.html'

    def get(self, request, *args, **kwargs):

        search = self.request.GET.get('search', '')

        contacts_list = Contact.from_curr_user.find_potential_contacts(self.request.user)

        if search:
            contacts_list = Contact.from_curr_user.search(self.request.user, search)

        context = super().get_context_data(**kwargs)

        invites = Invite.objects.filter(
            from_contact=self.request.user.contact_id
        ).values(
            'to_contact',
            'status'
        )

        context['invites_map'] = {invite.get('to_contact'): invite.get('status') for invite in invites}
        context['contact_list'] = contacts_list

        return self.render_to_response(context)