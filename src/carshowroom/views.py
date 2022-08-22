from django.shortcuts import render  # noqa F401
from rest_framework import mixins, viewsets
from .serializers import (
    CarShowroomSerializer,
    CarShowroomPresenceSerializer,
    CarSellsSerializer,
    CarBuyersSerializer,
    CarShowroomSalesSerializer,
)
from .models import (
    CarShowroom,
    CarShowroomPresence,
    CarSells,
    CarShowroomBuyers,
    CarShowroomSales,
)
from .filters import (
    CarShowroomFilter,
    CarShowroomPresenceFilter,
    CarShowroomBuyersFilter,
    CarShowroomSalesFilter,
)
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter, SearchFilter


class CarShowroomViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = CarShowroom.objects.all()
    serializer_class = CarShowroomSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = CarShowroomFilter
    ordering_fields = ["name", "create_time", "update_time", "location", "balance"]
    search_fields = ["name", "wishes", "wish_cars__choice_car__car__model__model"]


class CarShowroomPresenceViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = CarShowroomPresence.objects.all()
    serializer_class = CarShowroomPresenceSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = CarShowroomPresenceFilter
    ordering_fields = [
        "showroom__name",
        "create_time",
        "update_time",
        "car__model__model",
        "amount",
        "price",
    ]
    search_fields = ["showroom__name", "car__model__model", "supplier__name"]


class CarSellsViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = CarSells.objects.all()
    serializer_class = CarSellsSerializer


class CarBuyersViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = CarShowroomBuyers.objects.all()
    serializer_class = CarBuyersSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = CarShowroomBuyersFilter
    ordering_fields = [
        "showroom__name",
        "buyer__last_name",
        "create_time",
        "update_time",
        "sum_amount",
    ]
    search_fields = ["showroom__name", "buyer__last_name"]


class CarShowroomSalesViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = CarShowroomSales.objects.all()
    serializer_class = CarShowroomSalesSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = CarShowroomSalesFilter
    ordering_fields = [
        "title",
        "showroom__name",
        "discount",
        "create_time",
        "update_time",
        "date_start",
        "date_end",
    ]
    search_fields = ["title", "showroom__name"]
