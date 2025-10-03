import logging
from datetime import datetime

# Configure logger
logging.basicConfig(
    filename='requests.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the user and request path
        user = request.user.username if request.user.is_authenticated else 'Anonymous'
        
        # Log the request details
        logging.info(f"User: {user} - Path: {request.path}")
        
        # Call the next middleware or view
        response = self.get_response(request)
        return response
