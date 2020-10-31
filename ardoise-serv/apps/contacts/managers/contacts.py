from django.db import models
from django.db.models import Q


class ContactQuerySet(models.QuerySet):

    def search(self, search):
        return self.filter(
            Q(first_name__contains=search) |
            Q(last_name__contains=search) |
            Q(email__contains=search)
        )


class ContactsUserManager(models.Manager):

    def find_potential_contacts(self, user):
        return self.exclude(pk=user.contact_id)

    def search(self, user, search):
        return self.find_potential_contacts(user.contact_id).search(search)
