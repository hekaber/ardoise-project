from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.contacts.models import Contact


class InviteStatusEnum(models.TextChoices):
    PENDING = 'IPE', _('Invitation pending')
    VALIDATED = 'IVA', _('Invitation validated')
    CANCELLED = 'ICA', _('invitation_cancelled')
    DENIED = 'IDE', _('invitation_denied')


class Invite(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    from_contact = models.ForeignKey(Contact, related_name='%(class)s_related_from', on_delete=models.CASCADE)
    to_contact = models.ForeignKey(Contact, related_name='%(class)s_related_to', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default=InviteStatusEnum.PENDING, choices=InviteStatusEnum.choices)

    class Meta:
        db_table = 'invite'
        ordering = ['created']
