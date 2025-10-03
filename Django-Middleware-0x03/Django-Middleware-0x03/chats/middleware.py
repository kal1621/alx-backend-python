from django.http import HttpResponseForbidden

class RolePermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check for admin or moderator roles
        if not self.has_permission(request):
            return HttpResponseForbidden("You do not have permission to perform this action.")

        # Call the next middleware or view
        response = self.get_response(request)
        return response

    def has_permission(self, request):
        """Check if the user has the required role."""
        user = request.user
        # Assuming user roles are stored in user profile or as a field
        return user.is_authenticated and (user.is_admin or user.is_moderator)
