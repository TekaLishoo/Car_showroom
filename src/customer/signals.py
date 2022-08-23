from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import transaction
from django.dispatch import receiver
from src.customer.tasks import customer_buy_car
from src.customer.models import Customer


@receiver(post_save, sender="customer.CustomerOffer")
def customeroffer_after_saving(sender, instance, **kwargs):
    """
    Find cars and supplier with the best price
    which suits car showroom's preferences
    after creating a showroom.
    """
    transaction.on_commit(
        lambda: customer_buy_car.apply_async(
            args=(
                instance.buyer.id,
                instance.car.id,
                instance.max_price,
            )
        )
    )

#
# @receiver(post_save, sender=User)
# def create_customer(sender, instance, created, **kwargs):
#     if created:
#         Customer.objects.create(user=instance)
#     instance.customer.save()


