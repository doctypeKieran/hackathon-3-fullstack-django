# Generated by Django 4.2.7 on 2023-11-27 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user1', '0002_alter_userprofile_age_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(blank=True, default='Not Provided', max_length=15, null=True),
        ),
    ]
