# Generated by Django 4.2 on 2023-05-04 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_review_images'),
        ('favourites', '0003_remove_favourite_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='favourite',
            name='reviews',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='reviews.review'),
        ),
    ]
