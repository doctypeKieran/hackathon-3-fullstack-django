# Generated by Django 4.2.7 on 2023-11-28 16:08

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_delete_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='rageroomsession',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]