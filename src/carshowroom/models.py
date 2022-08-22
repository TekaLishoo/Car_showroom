from django.db import models
from django_countries.fields import CountryField
from src.core.models import CommonPart
from src.core.wishes import default_showroom_wishes
from django.core import validators
from djmoney.models.fields import MoneyField


class CarShowroom(CommonPart):
    """
    A model of a carshowroom.
    """

    name = models.CharField(max_length=100)
    location = CountryField(blank_label="(select country)")
    wishes = models.JSONField(null=True, blank=True, default=default_showroom_wishes)
    wish_cars = models.ManyToManyField("supplier.Car", blank=True, through="CarsChoice")
    balance = MoneyField(
        max_digits=19, decimal_places=4, default_currency="USD", default=500000
    )
    margin = models.PositiveIntegerField(
        validators=[validators.MaxValueValidator(100)], default=5
    )

    def __str__(self):
        return f"{self.name}, {self.location}"


class CarsChoice(CommonPart):
    """
    Model performs a preferred cars and its suppliers for each carshowroom.

    Records are created once carshowroom has been saved.
    """

    showroom = models.ForeignKey(
        CarShowroom, related_name="choice_showroom", on_delete=models.CASCADE
    )
    car = models.ForeignKey(
        "supplier.Car", related_name="choice_car", on_delete=models.CASCADE
    )
    wish_supplier = models.ForeignKey(
        "supplier.Supplier",
        related_name="choice_supplier",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    price = models.PositiveIntegerField(null=True)
    discount = models.PositiveIntegerField(
        null=True, validators=[validators.MaxValueValidator(100)]
    )

    def __str__(self):
        return f"{self.showroom}, {self.car.model.model}, {self.wish_supplier}"


class CarShowroomPresence(CommonPart):
    """
    Model performs which cars are presence in carshoomroom.
    """

    showroom = models.ForeignKey(
        CarShowroom, related_name="presence_showroom", on_delete=models.CASCADE
    )
    car = models.ForeignKey(
        "supplier.Car", related_name="presence_showroom_car", on_delete=models.CASCADE
    )
    amount = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    supplier = models.ForeignKey(
        "supplier.Supplier",
        related_name="presence_showroom_supplier",
        on_delete=models.SET("supplier deleted"),
    )

    def __str__(self):
        return f"{self.showroom.name}, {self.car.model.model}, {self.amount}"


class CarSells(CommonPart):
    """
    A list of sells of carshowroom.
    """

    showroom = models.ForeignKey(
        CarShowroom, related_name="carsells_showroom", on_delete=models.CASCADE
    )
    buyer = models.ForeignKey(
        "customer.Customer",
        related_name="carsells_customer",
        on_delete=models.SET("buyer deleted"),
    )
    car = models.ForeignKey(
        "supplier.Car", related_name="carsells_car", on_delete=models.CASCADE
    )
    amount = models.PositiveIntegerField()
    price = models.PositiveIntegerField()


class CarShowroomBuyers(CommonPart):
    """
    A list of customers of carshowroom.
    """

    showroom = models.ForeignKey(
        CarShowroom, related_name="buyers_showroom", on_delete=models.CASCADE
    )
    buyer = models.ForeignKey(
        "customer.Customer", related_name="buyers_customer", on_delete=models.CASCADE
    )
    sum_amount = models.PositiveIntegerField()


class CarShowroomSales(CommonPart):
    """
    A list of sales of carshowroom.
    """

    title = models.CharField(max_length=200)
    description = models.TextField()
    showroom = models.ForeignKey(
        CarShowroom, related_name="showroom_sales_showroom", on_delete=models.CASCADE
    )
    discount = models.PositiveIntegerField(
        validators=[validators.MaxValueValidator(100)]
    )
    cars = models.ManyToManyField("supplier.Car")
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
