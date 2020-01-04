# Generated by Django 2.2.3 on 2020-01-03 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20200103_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_post', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pictsagram/')),
                ('image_caption', models.CharField(max_length=700)),
                ('tag_someone', models.CharField(blank=True, max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('bio', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(upload_to='ProfilePicture/')),
                ('profile_avatar', models.ImageField(upload_to='AvatorPicture/')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='image',
            name='image_likes',
            field=models.ManyToManyField(blank=True, default=False, related_name='likes', to='core.Profile'),
        ),
        migrations.AddField(
            model_name='image',
            name='imageuploader_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentor', to='core.Profile'),
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Image'),
        ),
    ]
