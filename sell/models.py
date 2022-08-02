from django.db import models
from django_countries.fields import CountryField
from django.core import validators
import datetime


class CarShowroom(models.Model):
    name = models.CharField(max_length=100)
    location = CountryField(blank_label='(select country)')
    wish_body_type = models.ForeignKey('BodyType', related_name='showroom_body_type', on_delete=models.PROTECT)
    wish_engine_type = models.ForeignKey('EngineType', related_name='showroom_engine_type', on_delete=models.PROTECT)
    wish_drive_type = models.ForeignKey('DriveType', related_name='showroom_drive_type', on_delete=models.PROTECT)
    wish_cars = models.ManyToManyField('Car', blank=True)
    wish_supplier = models.ManyToManyField('Supplier', blank=True)
    balance = models.IntegerField(default=500000)
    create_time = models.TimeField(auto_now_add=True)
    update_time = models.TimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}, {self.location}'


class CarShowroomCarsPresence(models.Model):
    showroom = models.ForeignKey(CarShowroom, related_name='presence_showroom', on_delete=models.CASCADE)
    car = models.ForeignKey('Car', related_name='presence_showroom_car', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    price_per_one = models.PositiveIntegerField()
    supplier = models.ForeignKey('Supplier', related_name='presence_showroom_supplier',
                                 on_delete=models.SET('supplier deleted'))
    create_time = models.TimeField(auto_now_add=True)
    update_time = models.TimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class CarSells(models.Model):
    showroom = models.ForeignKey(CarShowroom, related_name='carsells_showroom', on_delete=models.CASCADE)
    buyer = models.ForeignKey('Buyer', related_name='carsells_buyer', on_delete=models.SET('buyer deleted'))
    car = models.ForeignKey('Car', related_name='carsells_car', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    price_per_one = models.PositiveIntegerField()
    create_time = models.TimeField(auto_now_add=True)
    update_time = models.TimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class CarShowroomBuyers(models.Model):
    showroom = models.ForeignKey(CarShowroom, related_name='buyers_showroom', on_delete=models.CASCADE)
    buyer = models.ForeignKey('Buyer', related_name='buyers_buyer', on_delete=models.CASCADE)
    sum_amount = models.PositiveIntegerField()
    create_time = models.TimeField(auto_now_add=True)
    update_time = models.TimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class CarShowroomSales(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    showroom = models.ForeignKey(CarShowroom, related_name='showroom_sales_showroom', on_delete=models.CASCADE)
    discount = models.PositiveIntegerField()
    cars = models.ManyToManyField('Car')
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    create_time = models.TimeField(auto_now_add=True)
    update_time = models.TimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class Buyer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=150)
    location = CountryField(blank_label='(select country)')
    balance = models.PositiveIntegerField()
    create_time = models.TimeField(auto_now_add=True)
    update_time = models.TimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.balance} USD'

class BuyerOffer(models.Model):
    buyer = models.ForeignKey(Buyer, related_name='offer_buyer', on_delete=models.CASCADE)
    car = models.ForeignKey('Car', related_name='offer_car', on_delete=models.CASCADE)
    max_price = models.PositiveIntegerField()
    create_time = models.TimeField(auto_now_add=True)
    update_time = models.TimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    location = CountryField(blank_label='(select country)')
    year_foundation = models.IntegerField(validators=[validators.MinValueValidator(1400),
                                                      validators.MaxValueValidator(datetime.date.today().year + 1),
                                                      ])
    amount_showrooms = models.PositiveIntegerField()
    create_time = models.TimeField(auto_now_add=True)
    update_time = models.TimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}, {self.year_foundation}, {self.location}'

class SupplierCarsPresence(models.Model):
    supplier = models.ForeignKey(Supplier, related_name='supplier_presence_supplier', on_delete=models.CASCADE)
    car = models.ForeignKey('Car', related_name='supplier_presence_car', on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    create_time = models.TimeField(auto_now_add=True)
    update_time = models.TimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class SupplierSales(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    supplier = models.ForeignKey(Supplier, related_name='supplier_sales_supplier', on_delete=models.CASCADE)
    discount = models.PositiveIntegerField()
    cars = models.ManyToManyField('Car')
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    create_time = models.TimeField(auto_now_add=True)
    update_time = models.TimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class Car(models.Model):
    TRANSMISSION_CHOICES = (
        ('Manual', 'Manual transmission'),
        ('Auto', 'Automatic transmission'),
    )
    FUEL_CHOICES = (
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    )

    model = models.ForeignKey('CarModel', related_name='car_model', on_delete=models.CASCADE)
    body_type = models.ForeignKey('BodyType', related_name='car_body_type', on_delete=models.PROTECT)
    engine_type = models.ForeignKey('EngineType', related_name='car_engine_type', on_delete=models.PROTECT)
    drive_type = models.ForeignKey('DriveType', related_name='car_drive_type', on_delete=models.PROTECT)
    transmission = models.CharField(max_length=50, choices=TRANSMISSION_CHOICES)
    engine_size = models.FloatField(validators=[validators.MinValueValidator(0),
                                                validators.MaxValueValidator(30),
                                                ])
    is_abs = models.BooleanField()
    fuel = models.CharField(max_length=20, choices=FUEL_CHOICES)
    is_parking_sensors = models.BooleanField()
    is_climate_control = models.BooleanField()
    is_cruise_control = models.BooleanField()
    is_heated_seats = models.BooleanField()
    doors = models.PositiveIntegerField(validators=[validators.MaxValueValidator(9)])
    seats = models.PositiveIntegerField(validators=[validators.MaxValueValidator(9)])

    def __str__(self):
        return f'{self.model}, {self.body_type}, {self.fuel}, {self.engine_size}'


class CarBrand(models.Model):
    brand = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.brand}'


class CarModel(models.Model):
    brand = models.ForeignKey(CarBrand, related_name='carmodel_brand', on_delete=models.CASCADE)
    model = models.CharField(max_length=50)


class BodyType(models.Model):
    body_type = models.CharField(max_length=20)


class EngineType(models.Model):
    engine_type = models.CharField(max_length=50)


class DriveType(models.Model):
    DRIVE_TYPE_CHOICES = (
        ('Rear', 'Rear drive'),
        ('front-wheel', 'front-wheel drive'),
        ('four-wheel', 'four-wheel drive'),
    )
    drive_type = models.CharField(max_length=15, choices=DRIVE_TYPE_CHOICES)
