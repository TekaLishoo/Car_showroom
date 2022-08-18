from django.core.management.base import BaseCommand
from src.carshowroom.models import CarShowroom
from faker import Faker
from django_countries import countries
from random import choice
from src.core.choices import BODY_TYPE_CHOICES, DRIVE_TYPE_CHOICES


class Command(BaseCommand):
    help = 'Create a given number of random showrooms'

    def add_arguments(self, parser):
        parser.add_argument('amount', nargs='+', type=int)

    def handle(self, *args, **options):
        for n in range(*options['amount']):
            showroom = CarShowroom()
            name = Faker().word().capitalize()
            while len(name) >= 100:
                name = Faker().word().capitalize()
            showroom.name = name
            showroom.location = choice(list(countries))
            wishes = {
                "body_type": choice(BODY_TYPE_CHOICES)[0],
                "drive_type": choice(DRIVE_TYPE_CHOICES)[0],
            }
            showroom.wishes = wishes
            showroom.balance = choice(range(300000, 2000000))
            showroom.margin = choice(range(1, 20))
            showroom.save()

        self.stdout.write(self.style.SUCCESS('Successfully created %s showrooms' % int(*options['amount'])))
