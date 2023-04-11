"""sdasdsd."""
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from rest_framework.response import Response

from .models import Comment, Post, User, Group

from .serializers import CommentSerializer, PostSerializer, UserSerializer,\
    GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Gsadada."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        instance.delete()


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """Gsadada."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Gsadada."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        """Create a new post."""
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user,
                        post=post)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        instance.delete()

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Gsadada."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def perform_create(self, serializer):
        """Create a new group."""
        if serializer.instance.author == 'admin':
            post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
            serializer.save(author=self.request.user, post=post)
        return Response(status=405)

    def perform_update(self, serializer):
        if serializer.instance.author == 'admin':
            if serializer.instance.author != self.request.user:
                raise PermissionDenied('Изменение чужого контента запрещено!')
            super(GroupViewSet, self).perform_update(serializer)
        return Response(status=405)
