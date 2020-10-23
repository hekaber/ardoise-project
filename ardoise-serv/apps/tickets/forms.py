from django import forms
from apps.contacts.models import Contact
from apps.shared.models import Currency


class TicketForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    owner = forms.CharField(widget=forms.HiddenInput())
    debtor = forms.ChoiceField()
    amount = forms.IntegerField(min_value=0)
    currency = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        contact_id = kwargs.pop('contact_id', None)
        super(TicketForm, self).__init__(*args, **kwargs)

        currencies_result = Currency.objects.all()
        currencies = [(lambda cur: (cur.id, cur.iso_code))(cur) for cur in currencies_result]
        self.fields['currency'].choices = currencies

        if contact_id:
            self.fields['owner'].initial = contact_id
            contacts_result = Contact.objects.get(pk=contact_id).contacts.all()
            contacts = [(lambda c: (c.id, c.email))(c) for c in contacts_result]
            self.fields['debtor'].choices = contacts
