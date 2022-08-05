from rest_framework import serializers
from .models import CarShowroom, CarShowroomPresence, CarSells, CarShowroomBuyers, CarShowroomSales


class CarShowroomSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)
    wish_cars = serializers.CharField(read_only=True)
    balance = serializers.CharField(read_only=True)
    wishes = serializers.JSONField()

    class Meta:
        model = CarShowroom
        fields = '__all__'


class CarShowroomPresenceSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = CarShowroomPresence
        fields = '__all__'


class CarSellsSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = CarSells
        fields = '__all__'


class CarBuyersSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = CarShowroomBuyers
        fields = '__all__'


class CarShowroomSalesSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = CarShowroomSales
        fields = '__all__'
