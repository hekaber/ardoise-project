from django.db import models


class User(models.Model):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
