# posts/urls.py

from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import PostViewSet, CommentViewSet

# Main router for posts
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

# Nested router for comments within posts
comments_router = routers.NestedSimpleRouter(router, r'posts', lookup='post')
comments_router.register(r'comments', CommentViewSet, basename='post-comments')

urlpatterns = router.urls + comments_router.urls