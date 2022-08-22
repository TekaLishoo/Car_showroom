from django.contrib import admin  # noqa F401
from .models import Customer, CustomerOffer

admin.site.register(Customer)
admin.site.register(CustomerOffer)
