from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)
    wishes = serializers.JSONField()

    class Meta:
        model = Customer
        fields = '__all__'
