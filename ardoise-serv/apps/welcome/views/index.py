from django.views import generic
from apps.contacts.models.invites import Invite


class IndexView(generic.TemplateView):

    template_name = 'welcome/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['counter'] = Invite.objects.count_invites(self.request.user.contact_id).first()
        return context
