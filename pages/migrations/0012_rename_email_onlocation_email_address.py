# Generated by Django 5.1.1 on 2024-11-19 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_onlocation_contact_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='onlocation',
            old_name='email',
            new_name='email_address',
        ),
    ]
