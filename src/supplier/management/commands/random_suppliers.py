from django.core.management.base import BaseCommand
from src.supplier.models import Supplier, SupplierCarsPresence, Car
from faker import Faker
from django_countries import countries
from random import choice
import datetime


class Command(BaseCommand):
    help = "Create a given number of random suppliers with a given number cars to sell"

    def add_arguments(self, parser):
        parser.add_argument("amount", nargs="+", type=int)
        parser.add_argument("amount_cars", nargs="+", type=int)

    def handle(self, *args, **options):
        for n in range(*options["amount"]):
            supplier = Supplier()
            name = Faker().word().capitalize()
            while len(name) >= 100:
                name = Faker().word().capitalize()
            supplier.name = name
            supplier.location = choice(list(countries))
            supplier.year_foundation = choice(
                range(1400, datetime.date.today().year + 1)
            )
            supplier.purchases_for_discount = choice(range(3, 11))
            supplier.discount_regular_customer = choice(range(1, 30))
            supplier.save()
            for i in range(*options["amount_cars"]):
                supplier_cars = SupplierCarsPresence()
                supplier_cars.supplier = supplier
                car = choice(Car.objects.all())
                exists_cars = SupplierCarsPresence.objects.filter(
                    supplier=supplier
                ).values_list("car", flat=True)
                while car.id in exists_cars:
                    car = choice(Car.objects.all())
                supplier_cars.car = car
                supplier_cars.price = choice(range(20000, 200000))
                supplier_cars.save()

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully created %s suppliers" % int(*options["amount"])
            )
        )
