# blog/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (
	PostListView, PostDetailView, PostCreateView, 
	PostUpdateView, PostDeleteView, 
	PostSearchView,
	tagged_posts_view,
    	PostByTagListView,
	CommentCreateView, CommentUpdateView, CommentDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('search/', PostSearchView.as_view(), name='post-search'),
    path('tags/<slug:tag_slug>/', tagged_posts_view, name='tagged-posts'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='tagged-posts'),

    # Comment URLs
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]