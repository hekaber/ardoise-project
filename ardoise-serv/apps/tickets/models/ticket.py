from django.db import models
from apps.contacts.models import Contact
from apps.shared.models import Currency
from django.utils.translation import gettext_lazy as _


class TicketStatusEnum(models.TextChoices):
    PENDING = 'TPE', _('ticket_pending')
    ONGOING = 'TON', _('ticket_ongoing')
    VALIDATED = 'TVA', _('ticket_validated')
    CANCELLED = 'TCA', _('ticket_cancelled')
    DENIED = 'TDE', _('ticket_denied')
    PAID = 'TPA', _('ticket_paid')


class Ticket(models.Model):

    name = models.CharField(max_length=255, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Contact, related_name='%(class)s_related_owner', on_delete=models.CASCADE)
    debtor = models.ForeignKey(Contact, related_name='%(class)s_related_debtor', null=True, on_delete=models.SET_NULL)
    amount = models.IntegerField()
    status = models.CharField(max_length=50, default=TicketStatusEnum.PENDING, choices=TicketStatusEnum.choices)
    currency = models.ForeignKey(Currency, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'ticket'
        ordering = ['created']
