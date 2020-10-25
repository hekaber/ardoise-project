# Generated by Django 3.1.2 on 2020-10-23 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0001_initial'),
        ('tickets', '0004_ticket_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shared.currency'),
        ),
    ]