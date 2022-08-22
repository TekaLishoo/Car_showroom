from django.shortcuts import render  # noqa F401
from rest_framework import mixins, viewsets
from .serializers import (
    SupplierSerializer,
    SupplierPresenceSerializer,
    SupplierSalesSerializer,
    CarSerializer,
    CarBrandSerializer,
    CarModelSerializer,
)
from .models import (
    Supplier,
    SupplierCarsPresence,
    SupplierSales,
    Car,
    CarBrand,
    CarModel,
)
from .filters import (
    SupplierFilter,
    SupplierCarPresenceFilter,
    SupplierSalesFilter,
    CarFilter,
)
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter, SearchFilter


class SupplierViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = SupplierFilter
    ordering_fields = [
        "name",
        "create_time",
        "update_time",
        "location",
        "year_foundation",
    ]
    search_fields = [
        "name",
    ]


class SupplierPresenceViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = SupplierCarsPresence.objects.all()
    serializer_class = SupplierPresenceSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = SupplierCarPresenceFilter
    ordering_fields = [
        "supplier__name",
        "create_time",
        "update_time",
        "car__model__model",
        "price",
    ]
    search_fields = ["supplier__name", "car__model__model"]


class SupplierSalesViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = SupplierSales.objects.all()
    serializer_class = SupplierSalesSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = SupplierSalesFilter
    ordering_fields = [
        "supplier__name",
        "create_time",
        "update_time",
        "discount",
        "date_start",
        "date_end",
    ]
    search_fields = ["supplier__name", "title"]


class CarViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = CarFilter
    ordering_fields = [
        "model__model",
        "body_type",
        "drive_type",
        "engine_size",
        "create_time",
        "update_time",
    ]
    search_fields = ["model__model", "color"]


class CarBrandViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class CarModelViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
