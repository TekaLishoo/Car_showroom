from django_filters import rest_framework as filters
from .models import Customer


class CustomerFilter(filters.FilterSet):
    body_type = filters.CharFilter(field_name='wishes__body_type', lookup_expr='icontains')
    drive_type = filters.CharFilter(field_name='wishes__drive_type', lookup_expr='icontains')

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'location',  'is_active']
