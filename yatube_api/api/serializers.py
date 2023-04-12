from rest_framework import serializers

from posts.models import Comment, Post, Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:

        model = Comment
        fields = ('id', 'text', 'author', 'post', 'created')
        read_only_fields = ('author', 'post',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:

        model = Group
        fields = ('id', 'title', 'slug', 'description')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, required=False)

    class Meta:

        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'image',
                  'group', 'comments')
