from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Custom permission to only allow owners to access their own messages.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user  # Assuming 'owner' is the user field in your Message model
