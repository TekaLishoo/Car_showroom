from django.shortcuts import render  # noqa F401
from rest_framework import mixins, viewsets
from .serializers import SupplierSerializer, SupplierPresenceSerializer, SupplierSalesSerializer, CarSerializer, \
    CarBrandSerializer, CarModelSerializer
from .models import Supplier, SupplierCarsPresence, SupplierSales, Car, CarBrand, CarModel


class SupplierViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierPresenceViewSet(mixins.ListModelMixin,
                              mixins.RetrieveModelMixin,
                              viewsets.GenericViewSet):
    queryset = SupplierCarsPresence.objects.all()
    serializer_class = SupplierPresenceSerializer


class SupplierSalesViewSet(mixins.CreateModelMixin,
                           mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    queryset = SupplierSales.objects.all()
    serializer_class = SupplierSalesSerializer


class CarViewSet(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarBrandViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class CarModelViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
