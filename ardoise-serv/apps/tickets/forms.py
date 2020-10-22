from django import forms
from apps.contacts.models import Contact


class TicketForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    owner = forms.CharField(widget=forms.HiddenInput())
    debtor = forms.ChoiceField()
    amount = forms.IntegerField(min_value=0)

    def __init__(self, *args, **kwargs):
        contact_id = kwargs.pop('contact_id', None)
        super(TicketForm, self).__init__(*args, **kwargs)

        if contact_id:
            self.fields['owner'].initial = contact_id
            contacts_result = Contact.objects.get(pk=contact_id).contacts.all()
            contacts = [(lambda c: (c.id, c.email))(c) for c in contacts_result]
            self.fields['debtor'].choices = contacts
