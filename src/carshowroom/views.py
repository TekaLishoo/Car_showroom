from django.shortcuts import render  # noqa F401
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from .serializers import (
    CarShowroomSerializer,
    CarShowroomPresenceSerializer,
    CarSellsSerializer,
    CarsBoughtAmountSerializer,
    CustomerSpentMoneySerializer,
    ShowroomNumberOfSellsSerializer,
    ShowroomProfitSerializer,
    ShowroomUniqueCustomersSerializer,
    ShowroomByLocationSerializer,
    CarBuyersSerializer,
    CarShowroomSalesSerializer,
    ShowroomUniqueSuppliersSerializer,
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
from rest_framework.response import Response
from rest_framework import status


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

    @action(
        methods=["get"], detail=True, serializer_class=ShowroomNumberOfSellsSerializer
    )
    def number_of_sells(self, request, pk=None):
        """
        <api/carshowrooms/<pk>/number_of_sells/
        will return a sum of sells for this particular showroom
        """
        serializer = self.get_serializer(data=request.data, context={"showroom_id": pk})
        if serializer.is_valid():
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)

    @action(methods=["get"], detail=True, serializer_class=ShowroomProfitSerializer)
    def profit(self, request, pk=None):
        """
        <api/carshowrooms/<pk>/profit/
        will return a total profit for this particular showroom
        """
        serializer = self.get_serializer(data=request.data, context={"showroom_id": pk})
        if serializer.is_valid():
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)

    @action(
        methods=["get"], detail=True, serializer_class=ShowroomUniqueCustomersSerializer
    )
    def unique_customers(self, request, pk=None):
        """
        <api/carshowrooms/<pk>/unique_customers/
        will return all unique customers for this particular showroom
        """
        serializer = self.get_serializer(data=request.data, context={"showroom_id": pk})
        if serializer.is_valid():
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)

    @action(
        methods=["get"], detail=False, serializer_class=ShowroomByLocationSerializer
    )
    def by_locations(self, request, pk=None):
        """
        <api/carshowrooms/by_locations/
        will return all distinct locations with amount of showrooms
        situated there
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)

    @action(
        methods=["get"], detail=True, serializer_class=ShowroomUniqueSuppliersSerializer
    )
    def unique_suppliers(self, request, pk=None):
        """
        <api/carshowrooms/<pk>/unique_suppliers/
        will return all unique suppliers this particular showroom was dealing with
        """
        serializer = self.get_serializer(data=request.data, context={"showroom_id": pk})
        if serializer.is_valid():
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)


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

    @action(methods=["get"], detail=False, serializer_class=CarsBoughtAmountSerializer)
    def total(self, request, pk=None):
        """
        <api/carsells/total/
        will return all distinct car with amount of items that were bought
        in descending order
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)

    @action(
        methods=["get"], detail=False, serializer_class=CustomerSpentMoneySerializer
    )
    def profit_customers(self, request, pk=None):
        """
        <api/carsells/profit_customers/
        will return all distinct customers with total spent by them money amount
        in descending order
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)


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
