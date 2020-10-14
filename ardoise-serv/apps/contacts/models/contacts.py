import uuid

from django.db import models


class Contact(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    public_id = models.CharField(max_length=255, default=str(uuid.uuid4()))

    class Meta:
        db_table = 'contact'
        ordering = ['created']
