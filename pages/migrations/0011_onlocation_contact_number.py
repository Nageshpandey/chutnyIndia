# Generated by Django 5.1.1 on 2024-11-19 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_onlocation_attandence_onlocation_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlocation',
            name='contact_number',
            field=models.CharField(default='', max_length=15),
        ),
    ]