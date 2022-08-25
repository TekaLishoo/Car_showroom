from rest_framework import serializers
from .models import (
    CarShowroom,
    CarShowroomPresence,
    CarSells,
    CarShowroomBuyers,
    CarShowroomSales,
)
from django.db.models import Sum, F, Count


class CarShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarShowroom
        fields = "__all__"
        read_only_fields = ("wish_cars", "balance")


class CarShowroomPresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarShowroomPresence
        fields = "__all__"


class CarSellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSells
        fields = "__all__"


class CarBuyersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarShowroomBuyers
        fields = "__all__"


class CarShowroomSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarShowroomSales
        fields = "__all__"


class ShowroomNumberOfSellsSerializer(serializers.ModelSerializer):
    number_of_sales = serializers.SerializerMethodField()

    class Meta:
        model = CarShowroom
        fields = ("number_of_sales",)

    def get_number_of_sales(self, *args, **kwargs):
        return CarSells.objects.filter(showroom=self.context['showroom_id']).values('showroom').annotate(Sum('amount'))


class ShowroomProfitSerializer(serializers.ModelSerializer):
    profit = serializers.SerializerMethodField()

    class Meta:
        model = CarShowroom
        fields = ("profit",)

    def get_profit(self, *args, **kwargs):
        return CarSells.objects.filter(showroom=self.context['showroom_id']).values('showroom').annotate(
            profit_sum=Sum(F('amount')*F('price')))


class ShowroomUniqueCustomersSerializer(serializers.ModelSerializer):
    unique_customers = serializers.SerializerMethodField()

    class Meta:
        model = CarShowroom
        fields = ("unique_customers",)

    def get_unique_customers(self, *args, **kwargs):
        return CarSells.objects.filter(showroom=self.context['showroom_id'])\
            .values('buyer__first_name', 'buyer__last_name').distinct()


class ShowroomByLocationSerializer(serializers.ModelSerializer):
    showrooms_location = serializers.SerializerMethodField()

    class Meta:
        model = CarShowroom
        fields = ("showrooms_location",)

    def get_showrooms_location(self, *args, **kwargs):
        return CarShowroom.objects.values('location').annotate(Count('id'))


class ShowroomUniqueSuppliersSerializer(serializers.ModelSerializer):
    unique_suppliers = serializers.SerializerMethodField()

    class Meta:
        model = CarShowroom
        fields = ("unique_suppliers",)

    def get_unique_suppliers(self, *args, **kwargs):
        return CarShowroomPresence.objects.filter(showroom=self.context['showroom_id'])\
            .values('supplier__name').distinct()


class CarsBoughtAmountSerializer(serializers.ModelSerializer):
    amount_cars = serializers.SerializerMethodField()

    class Meta:
        model = CarSells
        fields = ("amount_cars",)

    def get_amount_cars(self, *args, **kwargs):
        return CarSells.objects.values('car').annotate(Sum('amount')).order_by('-amount__sum')


class CustomerSpentMoneySerializer(serializers.ModelSerializer):
    spent_money = serializers.SerializerMethodField()

    class Meta:
        model = CarSells
        fields = ("spent_money",)

    def get_spent_money(self, *args, **kwargs):
        return CarSells.objects.values('buyer').annotate(spent_sum=Sum(F('amount')*F('price'))).order_by('-spent_sum')
