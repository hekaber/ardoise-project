# Generated by Django 3.1.2 on 2020-10-25 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0004_status_statuscategory'),
        ('contacts', '0014_auto_20201022_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='public_id',
            field=models.CharField(default='6791fc8a-fa6b-424a-b60e-dede5d9da1a5', max_length=255),
        ),
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('from_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invite_related_from', to='contacts.contact')),
                ('status', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shared.status')),
                ('to_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invite_related_to', to='contacts.contact')),
            ],
            options={
                'db_table': 'invite',
                'ordering': ['created'],
            },
        ),
    ]
