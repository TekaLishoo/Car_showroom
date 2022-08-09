from django.contrib import admin # noqa F401
from .models import CarShowroom, CarShowroomSales

admin.site.register(CarShowroom)
admin.site.register(CarShowroomSales)
