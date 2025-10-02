from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Notification

class MessagingTests(TestCase):
    def setUp(self):
        self.sender = User.objects.create(username='sender')
        self.receiver = User.objects.create(username='receiver')

    def test_notification_creation(self):
        message = Message.objects.create(sender=self.sender, receiver=self.receiver, content='Hello!')
        notifications = Notification.objects.filter(user=self.receiver)
        self.assertEqual(notifications.count(), 1)
        self.assertEqual(notifications.first().message, message)
