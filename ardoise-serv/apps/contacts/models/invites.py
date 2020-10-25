from django.db import models
from apps.contacts.models import Contact
from apps.shared.models import Status

DEFAULT_INVITE_ID = 1


class Invite(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    from_contact = models.ForeignKey(Contact, related_name='%(class)s_related_from', on_delete=models.CASCADE)
    to_contact = models.ForeignKey(Contact, related_name='%(class)s_related_to', on_delete=models.CASCADE)
    status = models.ForeignKey(Status, default=DEFAULT_INVITE_ID, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'invite'
        ordering = ['created']
