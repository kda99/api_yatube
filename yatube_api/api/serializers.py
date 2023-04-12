from rest_framework import serializers

from posts.models import Comment, CommentPost, Post, User, Group


class UserSerializer(serializers.ModelSerializer):

    posts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:

        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'posts')
        ref_name = 'ReadOnlyUsers'


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

    def create(self, validated_data):
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
