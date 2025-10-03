from rest_framework.permissions import BasePermission

class IsAuthenticatedAndParticipant(BasePermission):
    """
    Custom permission to only allow participants of a conversation to access messages.
    """

    def has_permission(self, request, view):
        # Allow only authenticated users
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow access only if the user is a participant in the conversation
        return request.user in obj.conversation.participants.all()  # Assuming the 'conversation' relation exists
