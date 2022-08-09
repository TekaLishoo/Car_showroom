from django_filters import rest_framework as filters
from .models import CarShowroom, CarShowroomPresence, CarShowroomBuyers, CarShowroomSales


class CarShowroomFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    body_type = filters.CharFilter(field_name='wishes__body_type')
    drive_type = filters.CharFilter(field_name='wishes__drive_type')
    engine_size = filters.CharFilter(field_name='wishes__engine_size', lookup_expr='icontains')
    min_balance = filters.NumberFilter(field_name="balance", lookup_expr='gte')
    max_balance = filters.NumberFilter(field_name="balance", lookup_expr='lte')

    class Meta:
        model = CarShowroom
        fields = ['location', 'is_active']


class CarShowroomPresenceFilter(filters.FilterSet):
    showroom = filters.CharFilter(field_name='showroom__name', lookup_expr='icontains')
    model = filters.CharFilter(field_name='car__model__model', lookup_expr='icontains')
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    supplier = filters.CharFilter(field_name='supplier__name', lookup_expr='icontains')

    class Meta:
        model = CarShowroomPresence
        fields = ['amount', 'is_active']


class CarShowroomBuyersFilter(filters.FilterSet):
    class Meta:
        model = CarShowroomBuyers
        fields = ['showroom__name', 'buyer__last_name']


class CarShowroomSalesFilter(filters.FilterSet):
    showroom = filters.CharFilter(field_name='showroom__name', lookup_expr='icontains')
    min_discount = filters.NumberFilter(field_name="discount", lookup_expr='gte')
    max_discount = filters.NumberFilter(field_name="discount", lookup_expr='lte')

    class Meta:
        model = CarShowroomSales
        fields = ['is_active']
