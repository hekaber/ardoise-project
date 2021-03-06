from django.db import models


class Currency(models.Model):

    iso_code = models.CharField(max_length=3, default='')

    class Meta:
        db_table = 'currency'
        ordering = ['iso_code']


class Country(models.Model):

    iso_code = models.CharField(max_length=5, default='')
    country_label = models.CharField(max_length=100, default='')
    currency = models.ForeignKey(Currency, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'country'

