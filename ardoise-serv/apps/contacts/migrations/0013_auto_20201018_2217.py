# Generated by Django 3.1.2 on 2020-10-18 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0012_auto_20201018_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='public_id',
            field=models.CharField(default='079f390d-62b0-4e28-82ed-60543d23d603', max_length=255),
        ),
    ]
