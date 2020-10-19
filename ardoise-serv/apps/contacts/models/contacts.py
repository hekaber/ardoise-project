import uuid

from django.db import models


class Contact(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(verbose_name='first name', max_length=30, blank=True)
    last_name = models.CharField(verbose_name='last name', max_length=30, blank=True)
    public_id = models.CharField(max_length=255, default=str(uuid.uuid4()))
    contacts = models.ManyToManyField(
        "self",
        through='ContactRelation',
        through_fields=('contact_a', 'contact_b')
    )

    class Meta:
        db_table = 'contact'
        ordering = ['created']

    def __str__(self):
        return self.email


class ContactRelation(models.Model):

    contact_a = models.ForeignKey(Contact, related_name='%(class)s_related_contact_a', on_delete=models.CASCADE)
    contact_b = models.ForeignKey(Contact, related_name='%(class)s_related_contact_b', on_delete=models.CASCADE)

    class Meta:
        db_table = 'contact_relation'
