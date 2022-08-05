from django.shortcuts import render # noqa F401
from rest_framework import mixins, viewsets
from .serializers import CustomerSerializer
from .models import Customer


class CustomerViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
