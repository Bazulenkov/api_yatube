from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('', include(router.urls)),
]
