from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='ProfilePicture/', null=True, blank=True)
    profile_avatar = models.ImageField(upload_to='AvatorPicture/', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name


class Image(models.Model):
    image = models.ImageField(upload_to='pictsagram/')
    image_caption = models.CharField(max_length=700)
    tag_someone = models.CharField(max_length=50, blank=True)
    imageuploader_profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image_likes = models.ManyToManyField('Profile', default=False, blank=True, related_name='likes')
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.image_caption + ' likes are'


class Comment(models.Model):
    comment_post = models.CharField(max_length=150)
    author = models.ForeignKey('Profile', related_name='commentor', on_delete=models.CASCADE)
    comment_image = models.ForeignKey('Image', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_post
