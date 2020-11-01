from django.views import generic
from apps.contacts.models.invites import Invite


class IndexView(generic.TemplateView):

    template_name = 'welcome/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['counter'] = {
                'pending': Invite.objects.get_pending_invites(self.request.user.contact_id).count(),
                'validated': Invite.objects.get_validated_invites(self.request.user.contact_id).count(),
                'cancelled': Invite.objects.get_cancelled_invites(self.request.user.contact_id).count(),
                'denied': Invite.objects.get_denied_invites(self.request.user.contact_id).count(),
            }
        return context
