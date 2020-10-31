# Generated by Django 3.1.2 on 2020-10-31 16:16

import apps.contacts.models.invites
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0015_auto_20201025_1732'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='contact',
            managers=[
                ('from_curr_user', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='public_id',
            field=models.CharField(default='8774c363-8c5a-4714-a7d0-b902190a92d7', max_length=255),
        ),
        migrations.AlterField(
            model_name='invite',
            name='status',
            field=models.CharField(choices=[(apps.contacts.models.invites.InviteStatusEnum['PENDING'], 'invitation_pending'), (apps.contacts.models.invites.InviteStatusEnum['VALIDATED'], 'invitation_validated'), (apps.contacts.models.invites.InviteStatusEnum['CANCELLED'], 'invitation_cancelled'), (apps.contacts.models.invites.InviteStatusEnum['DENIED'], 'invitation_denied')], default=apps.contacts.models.invites.InviteStatusEnum['PENDING'], max_length=50),
        ),
    ]
