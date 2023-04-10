"""serializers.py."""
from rest_framework import serializers

from .models import Comment, CommentPost, Post, User, Group


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model."""

    posts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        """Serializer for User model."""

        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'posts')
        ref_name = 'ReadOnlyUsers'


class CommentSerializer(serializers.ModelSerializer):
    """SASDSAD."""
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        """Serializer for comments."""

        model = Comment
        fields = ('id', 'text', 'author', 'post', 'created')
        read_only_fields = ('author', 'post',)


class GroupSerializer(serializers.ModelSerializer):
    """ASSAsaS."""

    # group_name = serializers.CharField(source='title')

    class Meta:
        """Serializer for groups."""

        model = Group
        fields = ('id', 'title', 'slug', 'description')


class PostSerializer(serializers.ModelSerializer):
    """aaSSaS."""
    author = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        """saassad."""

        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'comments', 'image',
                  'group')


    def create(self, validated_data):
        """sdadasdasd."""
        if 'comments' not in self.initial_data:
            post = Post.objects.create(**validated_data)
            return post
        else:
            comments = validated_data.pop('comments')
            post = Post.objects.create(**validated_data)
            for comment in comments:
                current_comment, status = Comment.objects.get_or_create(
                    **comment)
                CommentPost.objects.create(
                    comment=current_comment, post=post)
            return post
