# Generated by Django 3.1.2 on 2020-10-14 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20201014_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='public_id',
            field=models.CharField(default='e1e8ae85-2384-45af-93f7-8d4b4e630c44', max_length=255),
        ),
    ]