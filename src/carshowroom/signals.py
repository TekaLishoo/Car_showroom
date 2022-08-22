from django.db.models.signals import post_save
from django.dispatch import receiver
from src.supplier.models import Car, Supplier
from src.carshowroom.models import CarsChoice
from src.carshowroom.service import showroom_find_best_price


@receiver(post_save, sender="carshowroom.CarShowroom")
def run_after_saving(sender, instance, **kwargs):
    """
    Find cars and supplier with the best price
    which suits car showroom's preferences
    after creating a showroom.
    """
    if not (instance.wish_cars.exists()):
        for car in Car.objects.filter(is_active=True):
            if (
                instance.wishes["body_type"] == car.body_type
                and instance.wishes["drive_type"] == car.drive_type
            ):
                instance.wish_cars.add(car)
                sorted_prices = showroom_find_best_price(car.id)
                car_choice = CarsChoice.objects.get(showroom=instance, car=car)
                car_choice.wish_supplier = Supplier.objects.get(id=sorted_prices[0][0])
                car_choice.price = sorted_prices[0][1][0]
                car_choice.discount = sorted_prices[0][1][1]
                car_choice.save()
