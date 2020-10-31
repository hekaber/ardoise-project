from django.db import models
from apps.contacts.models import Contact
from apps.shared.utils import MEnum


class InviteStatusEnum(MEnum):
    PENDING = "invitation_pending"
    VALIDATED = "invitation_validated"
    CANCELLED = "invitation_cancelled"
    DENIED = "invitation_denied"


DEFAULT_INVITE_ID = InviteStatusEnum.PENDING


class Invite(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    from_contact = models.ForeignKey(Contact, related_name='%(class)s_related_from', on_delete=models.CASCADE)
    to_contact = models.ForeignKey(Contact, related_name='%(class)s_related_to', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default=InviteStatusEnum.PENDING, choices=InviteStatusEnum.get_choices())

    class Meta:
        db_table = 'invite'
        ordering = ['created']
