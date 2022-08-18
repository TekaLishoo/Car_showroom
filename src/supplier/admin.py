from django.contrib import admin # noqa F401
from .models import Supplier, Car, CarBrand, CarModel, SupplierCarsPresence, SupplierSales

admin.site.register(Supplier)
admin.site.register(Car)
admin.site.register(CarBrand)
admin.site.register(CarModel)
admin.site.register(SupplierCarsPresence)
admin.site.register(SupplierSales)
