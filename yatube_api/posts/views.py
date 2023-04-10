"""sdasdsd."""
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied

from .models import Comment, Post, User, Group

from .serializers import CommentSerializer, PostSerializer, UserSerializer,\
    GroupSerializer, PostListSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Gsadada."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Создание контента запрещено!')
        """Create a new post."""
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        instance.delete()

    # def get_serializer_class(self):
    #     # Если запрошенное действие (action) — получение списка объектов ('list')
    #     if self.action == 'list':
    #         # ...то применяем CatListSerializer
    #         return PostListSerializer
    #     # А если запрошенное действие — не 'list', применяем CatSerializer
    #     return PostSerializer


        # def get_queryset(self):
    #     post = get_object_or_404(Post, id=self.kwargs.get("post_id"))
    #     return post.comments.all()


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
        serializer.save(author=self.request.user, post = post)


class GroupViewSet(viewsets.ModelViewSet):
    """Gsadada."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
