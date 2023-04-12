from rest_framework import routers
from rest_framework.authtoken import views
from django.contrib import admin
from django.urls import include, path

from posts.views import CommentViewSet, PostViewSet, UserViewSet, GroupViewSet


router = routers.DefaultRouter()
router.register(r"api/v1/posts/(?P<post_id>\d+)/comments", CommentViewSet)
router.register(r'api/v1/posts', PostViewSet)
router.register(r'api/v1/groups', GroupViewSet)
router.register(r'api/v1/users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]
