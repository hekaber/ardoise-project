from django import forms
from apps.contacts.models import Invite


class InviteForm(forms.ModelForm):

    class Meta:
        model = Invite
        fields = ['to_contact']
