from apps.contacts.models import Contact, Invite, DEFAULT_INVITE_ID, INVITE_STATUS_CATEGORY
from apps.contacts.forms import InviteForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.views import generic


class InviteView(LoginRequiredMixin, generic.TemplateView):
    login_url = '/accounts/login/'
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
