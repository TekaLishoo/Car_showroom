from django.shortcuts import render  # noqa F401
from rest_framework import mixins, viewsets, permissions
from .serializers import CustomerSerializer, CustomerOfferSerializer
from .models import Customer, CustomerOffer
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


class CustomerOfferViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = CustomerOffer.objects.all()
    serializer_class = CustomerOfferSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
