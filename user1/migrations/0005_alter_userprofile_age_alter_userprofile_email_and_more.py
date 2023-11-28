# Generated by Django 4.2.7 on 2023-11-28 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user1', '0004_userprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='jesseross001@gmail.com', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(default='0124893232', max_length=15),
            preserve_default=False,
        ),
    ]
