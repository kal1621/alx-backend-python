from django.http import HttpResponseForbidden
from django.utils import timezone
import json

class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.message_count = {}
        self.blocked_ips = set()
        self.time_limit = 60  # Time limit in seconds
        self.max_messages = 5  # Max messages per time window

    def __call__(self, request):
        # Process only POST requests to the chat
        if request.method == 'POST' and 'message' in request.POST:
            ip_address = self.get_client_ip(request)
            current_time = timezone.now()

            # Initialize message count if not present
            if ip_address not in self.message_count:
                self.message_count[ip_address] = [0, current_time]

            count, first_message_time = self.message_count[ip_address]

            # Reset count if the time limit has passed
            if (current_time - first_message_time).total_seconds() > self.time_limit:
                self.message_count[ip_address] = [0, current_time]
                count = 0

            # Check for offensive language (simple example)
            if self.contains_offensive_language(request.POST['message']):
                return HttpResponseForbidden("Your message contains offensive language.")

            # Increment the message count
            count += 1
            self.message_count[ip_address][0] = count

            # Block if the limit is exceeded
            if count > self.max_messages:
                return HttpResponseForbidden("You have exceeded the message limit.")

        # Call the next middleware or view
        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        """Get the client's IP address from the request."""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')

    def contains_offensive_language(self, message):
        """Simple check for offensive language (you can expand this)."""
        offensive_words = {'badword1', 'badword2'}  # Add your offensive words here
        return any(word in message.lower() for word in offensive_words)
