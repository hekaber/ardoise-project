# Generated by Django 3.1.2 on 2020-10-18 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0011_auto_20201018_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='public_id',
            field=models.CharField(default='47b625d9-e1dd-4115-be70-78b46942fed5', max_length=255),
        ),
        migrations.AlterModelTable(
            name='contactrelation',
            table='contact_relation',
        ),
    ]
