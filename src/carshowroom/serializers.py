from rest_framework import serializers
from .models import CarShowroom, CarShowroomPresence, CarSells, CarShowroomBuyers, CarShowroomSales


class CarShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarShowroom
        fields = '__all__'
        read_only_fields = ('wish_cars', 'balance')


class CarShowroomPresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarShowroomPresence
        fields = '__all__'


class CarSellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSells
        fields = '__all__'


class CarBuyersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarShowroomBuyers
        fields = '__all__'


class CarShowroomSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarShowroomSales
        fields = '__all__'
