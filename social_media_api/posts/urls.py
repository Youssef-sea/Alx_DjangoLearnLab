# posts/urls.py

from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from django.urls import path
from .views import PostViewSet, CommentViewSet, FeedView, LikeUnlikeView

# Main router for posts
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

# Nested router for comments within posts
comments_router = routers.NestedSimpleRouter(router, r'posts', lookup='post')
comments_router.register(r'comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    path('feed/', FeedView.as_view(), name='user-feed'),
    path('posts/<int:pk>/like/', LikeUnlikeView.as_view(), name='post-like'),
    path('posts/<int:pk>/unlike/', LikeUnlikeView.as_view(), name='post-unlike'),
] + router.urls + comments_router.urls