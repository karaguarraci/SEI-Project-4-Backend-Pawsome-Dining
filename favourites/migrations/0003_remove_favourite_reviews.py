# Generated by Django 4.2 on 2023-05-04 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favourites', '0002_favourite_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourite',
            name='reviews',
        ),
    ]
