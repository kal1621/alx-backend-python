# views.py

from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Message

@cache_page(60)  # Cache the view for 60 seconds
def conversation_view(request):
    messages = Message.objects.select_related('sender', 'receiver').prefetch_related('replies')
    
    return render(request, 'chats/conversation.html', {'messages': messages})
