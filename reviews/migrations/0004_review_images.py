# Generated by Django 4.2 on 2023-04-22 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_rename_user_review_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
