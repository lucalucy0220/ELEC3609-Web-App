# Generated by Django 3.1.1 on 2020-10-29 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0015_profile_favourites'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='favourites',
            new_name='favorites',
        ),
    ]