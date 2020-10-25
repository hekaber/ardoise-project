from apps.contacts.models import Contact, Invite, DEFAULT_INVITE_ID
from apps.contacts.forms import InviteForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic


class InviteView(LoginRequiredMixin, generic.TemplateView):
    login_url = '/accounts/login/'
    template_name = 'contacts/invite.html'

    def post(self, request, *args, **kwargs):
        form = InviteForm(request.POST, contact_id=request.user.contact_id)
        if form.is_valid():
            invite = Invite()
            invite.from_contact = request.user.contact_id
            invite.to_contact = form.cleaned_data['owner']
            invite.status = DEFAULT_INVITE_ID
            invite.save()

        return render(request, 'contacts/invite.html', {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        invites = Invite.objects.filter(from_contact=self.request.user.contact_id).values_list('to_contact')

        context['current_invites'] = [inv[0] for inv in invites]
        context['contact_list'] = Contact.objects.all()
        return context
