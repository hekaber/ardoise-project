# Generated by Django 3.1.2 on 2020-10-23 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0002_auto_20201023_2211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currency',
            options={'ordering': ['iso_code']},
        ),
    ]
