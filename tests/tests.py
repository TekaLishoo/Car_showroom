import pytest
from django.urls import reverse
from src.carshowroom.service import sort_prices_according_all_discount, showroom_find_best_price
from src.supplier.models import (
    Supplier,
    Car,
    CarModel,
    CarBrand,
    SupplierCarsPresence
)
from src.core.choices import (
    TRANSMISSION_CHOICES,
    FUEL_CHOICES,
    DRIVE_TYPE_CHOICES,
    BODY_TYPE_CHOICES,
    COLOR_CHOICES,
)
from random import choice, randrange


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.mark.django_db
def test_unauthorized_request(api_client):
    """
    Check unauthorized API request
    """
    url = reverse("carshowroom-list")
    response = api_client.get(url)
    assert response.status_code == 401


@pytest.fixture
def example_prices():
    prices_tuple = (
        (1, (90000, 5, 5, 5)),
        (2, (50000, 0, 10, 20)),
        (3, (150000, 2, 1, 3)),
        (4, (86000, 7, 0, 6)),
        (5, (30000, 10, 0, 5)),
    )
    return prices_tuple


@pytest.fixture
def example_db():
    suppliers = Supplier.objects.bulk_create([
        Supplier(name='TestSupplier1', location='AD', year_foundation=1900),
        Supplier(name='TestSupplier2', location='AT', year_foundation=2000),
        Supplier(name='TestSupplier3', location='NZ', year_foundation=2010),
        Supplier(name='TestSupplier4', location='PL', year_foundation=1980),
        Supplier(name='TestSupplier5', location='GR', year_foundation=2005),
    ])
    brands = CarBrand.objects.bulk_create([
        CarBrand(brand='Brand1', ),
        CarBrand(brand='Brand2', ),
        CarBrand(brand='Brand3', ),
    ])
    models = CarModel.objects.bulk_create([
        CarModel(brand=brands[0], model='Model1'),
        CarModel(brand=brands[0], model='Model2'),
        CarModel(brand=brands[0], model='Model3'),
        CarModel(brand=brands[1], model='Model4'),
        CarModel(brand=brands[1], model='Model5'),
        CarModel(brand=brands[1], model='Model6'),
        CarModel(brand=brands[2], model='Model7'),
        CarModel(brand=brands[2], model='Model8'),
        CarModel(brand=brands[2], model='Model9'),
    ])
    for model in models:
        Car.objects.create(
            model=model,
            body_type=choice(BODY_TYPE_CHOICES)[0],
            drive_type=choice(DRIVE_TYPE_CHOICES)[0],
            transmission=choice(TRANSMISSION_CHOICES)[0],
            engine_size=randrange(0, 30),
            mileage=0,
            color=choice(COLOR_CHOICES)[0],
            fuel=choice(FUEL_CHOICES)[0],
            doors=5,
            seats=5,
        )
    car = Car.objects.get(id=1)
    price = 100000
    for supplier in suppliers:
        SupplierCarsPresence.objects.create(
            supplier=supplier,
            car=car,
            price=price,
        )
        price -= 10000


def test_sorting_prices(example_prices):
    """
    Test if function sort_prices_according_all_discount returns the best offer.
    """
    best_supplier, best_total_price = sort_prices_according_all_discount(example_prices)
    assert best_supplier == 5
    assert best_total_price == 25650


@pytest.mark.django_db
def test_showroom_find_best_price(example_db):
    """
    Test if the last offer which gives showroom_find_best_price
    is the least profitable.
    """
    assert showroom_find_best_price(1)[-1] == (1, [100000, 0])
