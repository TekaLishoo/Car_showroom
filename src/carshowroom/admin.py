from django.contrib import admin  # noqa F401
from .models import (
    CarShowroom,
    CarShowroomSales,
    CarsChoice,
    CarSells,
    CarShowroomPresence,
)

admin.site.register(CarShowroom)
admin.site.register(CarShowroomSales)
admin.site.register(CarsChoice)
admin.site.register(CarSells)
admin.site.register(CarShowroomPresence)
