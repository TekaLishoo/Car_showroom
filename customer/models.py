from django.db import models
from django_countries.fields import CountryField
from core.models import CommonPart
from core.wishes import default_customer_wishes
from djmoney.models.fields import MoneyField


class Customer(CommonPart):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=150)
    location = CountryField(blank_label="(select country)")
    balance = MoneyField(max_digits=19, decimal_places=4,
                         default_currency="USD")
    wishes = models.JSONField(null=True, default=default_customer_wishes)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.balance} USD"


class CustomerOffer(CommonPart):
    buyer = models.ForeignKey(
        Customer, related_name="offer_buyer", on_delete=models.CASCADE
    )
    car = models.ForeignKey(
        "supplier.Car", related_name="offer_car", on_delete=models.CASCADE
    )
    max_price = models.PositiveIntegerField()
