from rest_framework import serializers
from .models import Supplier, SupplierCarsPresence, SupplierSales, Car, CarBrand, CarModel


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class SupplierPresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierCarsPresence
        fields = '__all__'


class SupplierSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierSales
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'
