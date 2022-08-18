from celery import shared_task
from django.db.models import Sum
from djmoney.money import Money
from decimal import Decimal
from datetime import datetime
from dateutil.relativedelta import relativedelta
from src.carshowroom.models import CarShowroom, CarSells, CarsChoice, CarShowroomPresence
from src.carshowroom.service import (
    showroom_find_best_price,
    get_regular_customer_info,
    sort_prices_according_all_discount,
)
from src.supplier.models import Supplier, Car


@shared_task
def showroom_buy_cars():
    """
    Task runs every 10 minutes.
    Showrooms buy cars from their wishlist
    """
    # receive the history of car sells for last 2 months
    sells_history = CarSells.objects.values('car__id').annotate(sum_amount=Sum('amount')) \
        .filter(is_active=True, create_data__gte=datetime.today() + relativedelta(months=-2)) \
        .order_by('-sum_amount')
    for showroom in CarShowroom.objects.prefetch_related('wish_cars'):
        regular_customer_info = get_regular_customer_info(showroom)  # check for regular customer discount

        # make a list with cars to buy. Firstly buy cars which were bought more than others
        showroom_choice = showroom.wish_cars.values_list('id', flat=True)
        high_demand_cars = set(showroom_choice).intersection(set(sells_history.values_list('car__id', flat=True)))
        cars_to_buy = list(high_demand_cars)
        cars_to_buy.extend(list(set(showroom_choice).difference(high_demand_cars)))
        if len(cars_to_buy) != 0:
            for car_id in cars_to_buy:

                # check sales of suppliers
                sorted_prices = showroom_find_best_price(car_id)
                for k, v in enumerate(sorted_prices):
                    if sorted_prices[k][0] in list(regular_customer_info.keys()):
                        sorted_prices[k][1].extend(regular_customer_info[sorted_prices[k][0]])

                # get amount of car to buy
                try:
                    planned_num_cars = sells_history.get(car__id=car_id)['sum_amount']
                except ValueError:
                    planned_num_cars = 1

                # best price with actual sales
                best_supplier, best_total_price = sort_prices_according_all_discount(sorted_prices, planned_num_cars)

                # check balance and price of car
                if showroom.balance.amount >= best_total_price:
                    showroom.balance = Money(showroom.balance.amount - Decimal(best_total_price), 'USD')
                    showroom.save()
                    presence = CarShowroomPresence()
                    presence.showroom = showroom
                    presence.car = Car.objects.get(id=car_id)
                    presence.amount = planned_num_cars
                    presence.price = best_total_price / planned_num_cars * (1 + showroom.margin / 100)
                    presence.supplier = Supplier.objects.get(id=best_supplier)
                    presence.save()


@shared_task
def create_random_suppliers():
    return 'entered!!!'
