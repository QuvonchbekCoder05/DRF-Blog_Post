from rest_framework import serializers
from .models import Blog, Comment, Category, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'profile_image', 'bio', 'phone_number']


class BlogSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    like_count = serializers.ReadOnlyField()

    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'author', 'category', 'like_count', 'created_at']


class CommentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'blog', 'user', 'content', 'created_at']
