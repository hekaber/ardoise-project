# Generated by Django 3.1.2 on 2020-10-14 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contact_public_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='public_id',
            field=models.CharField(default='8fe0c33b-c7f5-4f1f-bf3f-4cdcbc0a2ffe', max_length=255),
        ),
    ]
