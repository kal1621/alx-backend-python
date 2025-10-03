from datetime import datetime
from django.http import HttpResponseForbidden

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour
        
        # Check if the current time is outside of 9 PM to 6 AM
        if current_hour < 6 or current_hour >= 21:
            return HttpResponseForbidden("Access to the chat is restricted at this hour.")
        
        # Call the next middleware or view
        response = self.get_response(request)
        return response
