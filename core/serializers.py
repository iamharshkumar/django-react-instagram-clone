from rest_framework import serializers
from .models import Profile, Image, Comment


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        serializers_class = Profile
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        serializers_class = Image
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        serializers_class = Comment
        fields = '__all__'
