from django.db import models


class InviteQuerySet(models.QuerySet):

    def search(self, search):
        return self.filter()

    def list(self, user):
        return self.exclude(user.contact_id)


class InviteManager(models.Manager):

    def find_invites(self, user):
        return self.exclude(pk=user.contact_id)

    def search(self, user, search):
        return self.find_contacts(user.contact_id).search(search)
