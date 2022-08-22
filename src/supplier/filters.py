from django_filters import rest_framework as filters
from .models import Supplier, SupplierCarsPresence, SupplierSales, Car


class SupplierFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    min_year = filters.NumberFilter(field_name="year_foundation", lookup_expr="gte")
    max_year = filters.NumberFilter(field_name="year_foundation", lookup_expr="lte")

    class Meta:
        model = Supplier
        fields = ["location", "is_active"]


class SupplierCarPresenceFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="supplier__name", lookup_expr="icontains")
    car = filters.CharFilter(field_name="car__model__model", lookup_expr="icontains")
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = SupplierCarsPresence
        fields = [
            "is_active",
        ]


class SupplierSalesFilter(filters.FilterSet):
    showroom = filters.CharFilter(field_name="supplier__name", lookup_expr="icontains")
    min_discount = filters.NumberFilter(field_name="discount", lookup_expr="gte")
    max_discount = filters.NumberFilter(field_name="discount", lookup_expr="lte")

    class Meta:
        model = SupplierSales
        fields = ["is_active"]


class CarFilter(filters.FilterSet):
    model = filters.CharFilter(field_name="model__model", lookup_expr="icontains")
    brand = filters.CharFilter(
        field_name="model__brand__brand", lookup_expr="icontains"
    )
    min_engine = filters.NumberFilter(field_name="engine_size", lookup_expr="gte")
    max_engine = filters.NumberFilter(field_name="engine_size", lookup_expr="lte")
    min_mileage = filters.NumberFilter(field_name="mileage", lookup_expr="gte")
    max_mileage = filters.NumberFilter(field_name="mileage", lookup_expr="lte")

    class Meta:
        model = Car
        fields = [
            "body_type",
            "drive_type",
            "transmission",
            "color",
            "is_abs",
            "fuel",
            "is_parking_sensors",
            "is_climate_control",
            "is_cruise_control",
            "is_heated_seats",
            "is_active",
        ]
