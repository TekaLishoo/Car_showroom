from django.db import models
from django_countries.fields import CountryField
from src.core.models import CommonPart
from src.core.wishes import default_customer_wishes
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User


class Customer(CommonPart):
    """
    A model of a customer.
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=150)
    location = CountryField(blank_label="(select country)")
    balance = MoneyField(max_digits=19, decimal_places=4, default_currency="USD")
    wishes = models.JSONField(null=True, default=default_customer_wishes)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.balance} USD"


class CustomerOffer(CommonPart):
    """
    A model of customer offer.
    """

    buyer = models.ForeignKey(
        Customer, related_name="offer_buyer", on_delete=models.CASCADE
    )
    car = models.ForeignKey(
        "supplier.Car", related_name="offer_car", on_delete=models.CASCADE
    )
    max_price = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if self.max_price <= self.buyer.balance.amount:
            super(CustomerOffer, self).save(*args, **kwargs)
        else:
            raise ValueError("Price is higher than customer's balance")
