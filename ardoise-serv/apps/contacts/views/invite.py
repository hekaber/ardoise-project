from apps.contacts.models import Contact, Invite
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import render, redirect


class InviteView(LoginRequiredMixin, generic.View):
    login_url = '/accounts/login/'

    def post(self, request, *args, **kwargs):
        contact_id = self.request.POST.get('contact', '')

        context = {'contact': None}
        if contact_id:
            context['contact'] = Contact.objects.get(pk=contact_id)

        return render(self.request, 'contacts/invite.html', context)


class InviteConfirmationView(LoginRequiredMixin, generic.View):

    def post(self, request, *args, **kwargs):
        contact_id = self.request.POST.get('contact', '')
        current_user_contact_id = self.request.user.contact_id

        context = {'contact': None}
        if contact_id:
            context['contact'] = Contact.objects.get(pk=contact_id)
            invite = Invite.objects.create(
                from_contact_id=current_user_contact_id,
                to_contact_id=contact_id
            )
            invite.save()

        return render(self.request, 'contacts/invite_confirm.html', context)
