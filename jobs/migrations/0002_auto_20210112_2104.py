# Generated by Django 2.0.2 on 2021-01-12 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='summry',
            new_name='summary',
        ),
    ]
