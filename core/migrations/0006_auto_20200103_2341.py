# Generated by Django 2.2.3 on 2020-01-03 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200103_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_avatar',
            field=models.ImageField(blank=True, null=True, upload_to='AvatorPicture/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='ProfilePicture/'),
        ),
    ]
