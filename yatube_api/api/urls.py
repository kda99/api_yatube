from rest_framework import routers
from rest_framework.authtoken import views
from django.urls import include, path

from .views import CommentViewSet, PostViewSet, GroupViewSet


router = routers.DefaultRouter()
router.register(r"api/v1/posts/(?P<post_id>\d+)/comments", CommentViewSet)
router.register(r'api/v1/posts', PostViewSet)
router.register(r'api/v1/groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]
