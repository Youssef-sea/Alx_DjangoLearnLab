# notifications/views.py

from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return all notifications for the authenticated user, ordered by timestamp
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')

class NotificationDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = NotificationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Notification.objects.all()

    def update(self, request, *args, **kwargs):
        # Allow marking a notification as read
        instance = self.get_object()
        if request.data.get('is_read'):
            instance.is_read = True
            instance.save()
            return Response(self.get_serializer(instance).data)
        return super().update(request, *args, **kwargs)