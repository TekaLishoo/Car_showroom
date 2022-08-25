from celery import shared_task
from src.carshowroom.models import CarShowroomPresence, CarSells
from src.customer.models import Customer
import datetime
from djmoney.money import Money
from decimal import Decimal


@shared_task
def customer_buy_car(buyer_id, car_id, max_price):
    # search for the best price
    prices = dict()
    offers = CarShowroomPresence.objects.filter(
        is_active=True, car__id=car_id, amount__gt=0
    ).select_related("showroom")
    for offer in offers:
        offer_discount = 0
        for sale in offer.showroom.showroom_sales_showroom.filter(
            is_active=True,
            date_start__lte=datetime.datetime.now(),
            date_end__gte=datetime.datetime.now(),
        ).prefetch_related("cars"):
            if car_id in sale.cars.values_list("id", flat=True):
                offer_discount = sale.discount
        prices[offer.showroom.id] = [offer.price, offer_discount]
    if len(prices) != 0:
        best_offer = sorted(
            prices.items(), key=lambda x: x[1][0] * (1 - x[1][1] / 100)
        )[0]
        best_showroom_offer = offers.filter(showroom__id=best_offer[0]).first()
        best_price = best_offer[1][0] * (1 - best_offer[1][1] / 100)
        actual_customer = Customer.objects.get(id=buyer_id)

        # if balance allows customer will buy a car
        if best_price <= actual_customer.balance.amount and best_price <= float(
            max_price
        ):
            actual_customer.balance = Money(
                actual_customer.balance.amount - Decimal(best_price), "USD"
            )
            actual_customer.save()

            # increase showroom balance
            best_showroom_offer.showroom.balance = Money(
                best_showroom_offer.showroom.balance.amount + Decimal(best_price), "USD"
            )
            best_showroom_offer.showroom.save()

            # decrease amount CarShowroomPresence
            best_showroom_offer.amount -= 1
            if best_showroom_offer.amount == 0:
                best_showroom_offer.is_active = False
            best_showroom_offer.save()

            # add to CarSells
            car_sell = CarSells()
            car_sell.showroom = best_showroom_offer.showroom
            car_sell.buyer = actual_customer
            car_sell.car = best_showroom_offer.car
            car_sell.amount = 1
            car_sell.price = best_price
            car_sell.save()
