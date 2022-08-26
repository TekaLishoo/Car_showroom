from django.core.management.base import BaseCommand
from src.customer.models import Customer, CustomerOffer
from src.supplier.models import Car
from faker import Faker
from django_countries import countries
from random import choice
from src.core.choices import BODY_TYPE_CHOICES, DRIVE_TYPE_CHOICES


class Command(BaseCommand):
    help = "Create a random customer offer"

    def handle(self, *args, **options):
        customer_offer = CustomerOffer()
        customer_offer.buyer = choice(Customer.objects.all())
        customer_offer.car = choice(Car.objects.all())
        customer_offer.max_price = customer_offer.buyer.balance.amount
        customer_offer.save()

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully created customer offer for %s" % customer_offer.buyer
            )
        )
