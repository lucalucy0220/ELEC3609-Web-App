# Generated by Django 3.1.1 on 2020-10-28 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0014_auto_20201023_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favourites',
            field=models.ManyToManyField(to='recipe.Post'),
        ),
    ]
