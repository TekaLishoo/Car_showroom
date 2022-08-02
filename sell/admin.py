from django.contrib import admin
from .models import Supplier, SupplierSales, CarShowroom, CarShowroomSales, Buyer, Car, CarBrand, CarModel, BodyType, \
    EngineType, DriveType

admin.site.register(Supplier)
admin.site.register(SupplierSales)
admin.site.register(CarShowroom)
admin.site.register(CarShowroomSales)
admin.site.register(Buyer)
admin.site.register(Car)
admin.site.register(CarBrand)
admin.site.register(CarModel)
admin.site.register(BodyType)
admin.site.register(EngineType)
admin.site.register(DriveType)
