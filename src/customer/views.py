from django.shortcuts import render  # noqa F401
from rest_framework import mixins, viewsets
from .serializers import CustomerSerializer
from .models import Customer
from .filters import CustomerFilter
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter, SearchFilter


class CustomerViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = CustomerFilter
    ordering_fields = [
        "first_name",
        "last_name",
        "create_time",
        "update_time",
        "location",
        "balance",
    ]
    search_fields = ["first_name", "last_name"]
