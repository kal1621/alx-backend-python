

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Message
from .serializers import MessageSerializer
from .permissions import IsAuthenticatedAndParticipant
from .filters import MessageFilter
from .pagination import MessagePagination  # Import your custom pagination class

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticatedAndParticipant]
    pagination_class = MessagePagination  # Use custom pagination class
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MessageFilter  # Use the filtering class

    def get_queryset(self):
        return self.queryset.filter(conversation__participants=self.request.user)
