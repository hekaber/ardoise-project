# Generated by Django 3.1.2 on 2020-10-25 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0003_auto_20201023_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('label', models.CharField(default='', max_length=100)),
            ],
            options={
                'db_table': 'status_category',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('label', models.CharField(default='', max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared.statuscategory')),
            ],
            options={
                'db_table': 'status',
            },
        ),
    ]