"""sdasdsd."""
from rest_framework import viewsets

from yatube_api.posts.models import Comment, Post, User, Group

from yatube_api.posts.serializers import CommentSerializer, PostSerializer,\
    UserSerializer, GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Gsadada."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """Create a new post."""
        serializer.save(author=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """Gsadada."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Gsadada."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """Gsadada."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
