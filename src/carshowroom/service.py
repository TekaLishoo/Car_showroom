from src.supplier.models import SupplierCarsPresence, SupplierSales, Supplier
from src.carshowroom.models import CarShowroomPresence
import datetime
from django.db.models import Sum


def showroom_find_best_price(car_id):
    """
    Checks for sales for each supplier car offer
    and returns a tuple with a supplier id
    and a list of price and discount (sorted in profitable order)
    """
    prices = dict()
    for offer in SupplierCarsPresence.objects.filter(is_active=True, car__id=car_id).select_related('supplier'):
        offer_discount = 0
        for sale in offer.supplier.supplier_sales_supplier.filter(is_active=True,
                                                                  date_start__lte=datetime.datetime.now(),
                                                                  date_end__gte=datetime.datetime.now()
                                                                  ).prefetch_related('cars'):
            if car_id in sale.cars.values_list('id', flat=True):
                offer_discount = sale.discount
        prices[offer.supplier.id] = [offer.price, offer_discount]
    return sorted(prices.items(), key=lambda x: x[1][0] * (1 - x[1][1] / 100))


def get_regular_customer_info(showroom):
    """
    For particular showroom returns a dictionary
    with supplier's ids as a keys and
    a list with amount of purchases needed to be done for become a regular customer
    and a discount of a regular customer as values.
    """
    number_sells_done = CarShowroomPresence.objects.filter(is_active=True, showroom=showroom).select_related(
        'supplier').values('supplier__id').annotate(Sum('amount'))
    number_sells_needed = Supplier.objects.filter(is_active=True).values('id', 'purchases_for_discount',
                                                                         'discount_regular_customer')
    number_sells_dict = {}
    for supplier in number_sells_needed:
        if supplier['id'] in number_sells_done.values_list('supplier__id', flat=True):
            number_sells_dict[supplier['id']] = [
                supplier['purchases_for_discount'] - number_sells_done.get(supplier__id=supplier['id'])['amount__sum'],
                supplier['discount_regular_customer']]
        else:
            number_sells_dict[supplier['id']] = [supplier['purchases_for_discount'],
                                                 supplier['discount_regular_customer']]
    return number_sells_dict


def sort_prices_according_all_discount(prices, cars_to_buy=1):
    """
    Returns a supplier id with the best offer and a total price
    """
    offers = dict()
    for offer in prices:
        price_sale = offer[1][0] * (1 - offer[1][1] / 100)
        if offer[1][2] > cars_to_buy or offer[1][3] == 0:
            offers[offer[0]] = cars_to_buy * price_sale
        elif offer[1][2] <= 0:
            offers[offer[0]] = cars_to_buy * price_sale * (1 - offer[1][3] / 100)
        else:
            offers[offer[0]] = offer[1][2] * price_sale + \
                               (cars_to_buy - offer[1][2]) * price_sale * (1 - offer[1][3] / 100)
    best_offer = sorted(offers.items(), key=lambda x: x[1])[0]
    return best_offer[0], best_offer[1]
