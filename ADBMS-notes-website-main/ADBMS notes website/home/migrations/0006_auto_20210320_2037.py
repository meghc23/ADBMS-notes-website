# Generated by Django 3.1.5 on 2021-03-20 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_profile_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='ph_number',
        ),
    ]
