import django_filters
from .models import Message

class MessageFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(field_name='sender__username', lookup_expr='exact')
    start_date = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')  # Change 'created_at' to your actual timestamp field
    end_date = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Message
        fields = ['user', 'start_date', 'end_date']
