# Generated by Django 4.1 on 2022-08-27 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0004_rename_datacollection_datacollected'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='datacollected',
            new_name='data',
        ),
    ]
