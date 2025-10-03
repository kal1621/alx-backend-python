from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer
from .permissions import IsAuthenticatedAndParticipant

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticatedAndParticipant]

    def get_queryset(self):
        # Only return messages that belong to the authenticated user's conversations
        return self.queryset.filter(conversation__participants=self.request.user)
