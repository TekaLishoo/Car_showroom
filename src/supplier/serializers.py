from rest_framework import serializers
from .models import Supplier, SupplierCarsPresence, SupplierSales, Car, CarBrand, CarModel


class SupplierSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = Supplier
        fields = '__all__'


class SupplierPresenceSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = SupplierCarsPresence
        fields = '__all__'


class SupplierSalesSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = SupplierSales
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = Car
        fields = '__all__'


class CarBrandSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = CarBrand
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = CarModel
        fields = '__all__'
