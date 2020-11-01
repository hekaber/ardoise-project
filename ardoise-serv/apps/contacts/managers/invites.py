from django.db import models
from django.db.models import Case, IntegerField, Sum, When


class InviteQuerySet(models.QuerySet):

    def get_pending_invites(self, contact_id):
        return self.filter(to_contact_id=contact_id, status=self.model.InviteStatusEnum.PENDING)

    def get_validated_invites(self, contact_id):
        return self.filter(to_contact_id=contact_id, status=self.model.InviteStatusEnum.VALIDATED)

    def get_cancelled_invites(self, contact_id):
        return self.filter(to_contact_id=contact_id, status=self.model.InviteStatusEnum.CANCELLED)

    def get_denied_invites(self, contact_id):
        return self.filter(to_contact_id=contact_id, status=self.model.InviteStatusEnum.DENIED)

    def get_sent_invites(self, contact_id):
        return self.filter(from_contact_id=contact_id)

    def list(self, user):
        return self.exclude(user.contact_id)
