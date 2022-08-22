from django.db import models
from django_countries.fields import CountryField
from django.core import validators
from src.core.models import CommonPart
from src.core.choices import (
    TRANSMISSION_CHOICES,
    FUEL_CHOICES,
    DRIVE_TYPE_CHOICES,
    BODY_TYPE_CHOICES,
    COLOR_CHOICES,
)
import datetime


class Supplier(CommonPart):
    """
    A model of a supplier.
    """

    name = models.CharField(max_length=100)
    location = CountryField(blank_label="(select country)")
    year_foundation = models.IntegerField(
        validators=[
            validators.MinValueValidator(1400),
            validators.MaxValueValidator(datetime.date.today().year + 1),
        ]
    )
    purchases_for_discount = models.PositiveIntegerField(default=5)
    discount_regular_customer = models.PositiveIntegerField(
        validators=[validators.MaxValueValidator(100)], default=5
    )

    def __str__(self):
        return f"{self.name}, {self.year_foundation}, {self.location}"


class SupplierCarsPresence(CommonPart):
    """
    Model performs which cars are sold by supplier.
    """

    supplier = models.ForeignKey(
        Supplier, related_name="supplier_presence_supplier", on_delete=models.CASCADE
    )
    car = models.ForeignKey(
        "Car", related_name="supplier_presence_car", on_delete=models.CASCADE
    )
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.supplier.name}, {self.car.model}, {self.price}"


class SupplierSales(CommonPart):
    """
    A list of sales of supplier.
    """

    title = models.CharField(max_length=200)
    description = models.TextField()
    supplier = models.ForeignKey(
        Supplier, related_name="supplier_sales_supplier", on_delete=models.CASCADE
    )
    discount = models.PositiveIntegerField(
        validators=[validators.MaxValueValidator(100)]
    )
    cars = models.ManyToManyField("Car")
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()

    def __str__(self):
        return f"{self.supplier.name}, {self.discount}%, {self.date_start} - {self.date_end}"


class Car(CommonPart):
    """
    A model of a car.
    """

    model = models.ForeignKey(
        "CarModel", related_name="car_model", on_delete=models.CASCADE
    )
    body_type = models.CharField(max_length=15, choices=BODY_TYPE_CHOICES)
    drive_type = models.CharField(max_length=15, choices=DRIVE_TYPE_CHOICES)
    transmission = models.CharField(max_length=50, choices=TRANSMISSION_CHOICES)
    engine_size = models.FloatField(
        validators=[
            validators.MinValueValidator(0),
            validators.MaxValueValidator(30),
        ]
    )
    mileage = models.PositiveIntegerField()
    color = models.CharField(max_length=15, choices=COLOR_CHOICES)
    is_abs = models.BooleanField(default=True)
    fuel = models.CharField(max_length=20, choices=FUEL_CHOICES)
    is_parking_sensors = models.BooleanField(default=True)
    is_climate_control = models.BooleanField(default=True)
    is_cruise_control = models.BooleanField(default=True)
    is_heated_seats = models.BooleanField(default=False)
    doors = models.PositiveIntegerField(validators=[validators.MaxValueValidator(9)])
    seats = models.PositiveIntegerField(validators=[validators.MaxValueValidator(9)])

    def __str__(self):
        return f"{self.model}, {self.body_type}, " f"{self.fuel}, {self.engine_size}"


class CarBrand(CommonPart):
    """
    A model of a car brand.
    """

    brand = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.brand}"


class CarModel(CommonPart):
    """
    A model of a car model.
    """

    brand = models.ForeignKey(
        CarBrand, related_name="carmodel_brand", on_delete=models.CASCADE
    )
    model = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.brand} {self.model}"
