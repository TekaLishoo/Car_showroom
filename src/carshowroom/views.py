from django.shortcuts import render  # noqa F401
from rest_framework import mixins, viewsets
from .serializers import CarShowroomSerializer, CarShowroomPresenceSerializer, CarSellsSerializer, CarBuyersSerializer, \
    CarShowroomSalesSerializer
from .models import CarShowroom, CarShowroomPresence, CarSells, CarShowroomBuyers, CarShowroomSales


class CarShowroomViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    queryset = CarShowroom.objects.all()
    serializer_class = CarShowroomSerializer


class CarShowroomPresenceViewSet(mixins.ListModelMixin,
                                 mixins.RetrieveModelMixin,
                                 viewsets.GenericViewSet):
    queryset = CarShowroomPresence.objects.all()
    serializer_class = CarShowroomPresenceSerializer


class CarSellsViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = CarSells.objects.all()
    serializer_class = CarSellsSerializer


class CarBuyersViewSet(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    queryset = CarShowroomBuyers.objects.all()
    serializer_class = CarBuyersSerializer


class CarShowroomSalesViewSet(mixins.CreateModelMixin,
                              mixins.ListModelMixin,
                              mixins.RetrieveModelMixin,
                              viewsets.GenericViewSet):
    queryset = CarShowroomSales.objects.all()
    serializer_class = CarShowroomSalesSerializer
