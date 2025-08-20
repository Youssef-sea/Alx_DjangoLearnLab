# posts/views.py

from rest_framework import viewsets, permissions, generics
from rest_framework.filters import SearchFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification 

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        post_id = self.kwargs['post_pk']
        post = Post.objects.get(pk=post_id)
        serializer.save(author=self.request.user, post=post)

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retrieve the users the current user is following.
        following_users = self.request.user.following.all()
        
        # Filter posts by those authors and order them by creation date.
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

class LikeUnlikeView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        user = request.user
        
        try:
            # Check if a like from this user on this post already exists
            like = Like.objects.get(user=user, post=post)
            like.delete()
            return Response({'message': 'Post unliked successfully.'}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            # If it doesn't exist, create a new one
            Like.objects.create(user=user, post=post)
            
            # Create a notification for the post's author
            if user != post.author:
                Notification.objects.create(
                    recipient=post.author,
                    actor=user,
                    verb='liked your post',
                    target=post
                )
            
            return Response({'message': 'Post liked successfully.'}, status=status.HTTP_201_CREATED)

generics.get_object_or_404(Post, pk=pk)", "Like.objects.get_or_create(user=request.user, post=post)"