from apps.contacts.models import Contact, Invite, DEFAULT_INVITE_ID, INVITE_STATUS_CATEGORY
from apps.shared.models import Status
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

        queryset = Contact.objects.exclude(pk=self.request.user.contact_id)

        if search:
            queryset = Contact.objects.filter((
                Q(first_name__contains=search) |
                Q(last_name__contains=search) |
                Q(email__contains=search)) &
                ~Q(pk=self.request.user.contact_id)
            )

        context = super().get_context_data(**kwargs)

        invites = Invite.objects.filter(
            from_contact=self.request.user.contact_id
        ).values(
            'to_contact',
            'status_id',
            'status__label'
        )

        context['invites_map'] = {invite.get('to_contact'): invite.get('status__label') for invite in invites}
        context['contact_list'] = queryset

        return self.render_to_response(context)
