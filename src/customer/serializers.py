from rest_framework import serializers
from .models import Customer, CustomerOffer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        read_only_fields = ("user", "is_active")


class CustomerOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOffer
        fields = "__all__"
        read_only_fields = ("buyer",)
