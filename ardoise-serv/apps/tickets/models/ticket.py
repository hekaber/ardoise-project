from django.db import models
from apps.contacts.models import Contact


class Ticket(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Contact, related_name='%(class)s_related_owner', on_delete=models.CASCADE)
    debtor = models.ForeignKey(Contact, related_name='%(class)s_related_debtor', null=True, on_delete=models.SET_NULL)
    amount = models.IntegerField(min_value=0)

    class Meta:
        db_table = 'ticket'
        ordering = ['created']
