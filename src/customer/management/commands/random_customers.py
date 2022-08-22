from django.core.management.base import BaseCommand
from src.customer.models import Customer
from faker import Faker
from django_countries import countries
from random import choice
from src.core.choices import BODY_TYPE_CHOICES, DRIVE_TYPE_CHOICES


class Command(BaseCommand):
    help = "Create a given number of random customers"

    def add_arguments(self, parser):
        parser.add_argument("amount", nargs="+", type=int)

    def handle(self, *args, **options):
        for n in range(*options["amount"]):
            customer = Customer()
            first_name = Faker().first_name()
            while len(first_name) >= 50:
                first_name = Faker().first_name()
            customer.first_name = first_name
            last_name = Faker().last_name()
            while len(last_name) >= 150:
                last_name = Faker().last_name()
            customer.last_name = last_name
            customer.location = choice(list(countries))
            customer.balance = choice(range(30000, 2000000))
            wishes = {
                "body_type": choice(BODY_TYPE_CHOICES)[0],
                "drive_type": choice(DRIVE_TYPE_CHOICES)[0],
                "is_heated_seats": choice(["True", "False"]),
            }
            customer.wishes = wishes
            customer.save()

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully created %s customers" % int(*options["amount"])
            )
        )
