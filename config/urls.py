"""car_showroom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from src.carshowroom.views import CarShowroomViewSet, CarShowroomPresenceViewSet, CarSellsViewSet, CarBuyersViewSet, \
    CarShowroomSalesViewSet
from src.supplier.views import SupplierViewSet, SupplierPresenceViewSet, SupplierSalesViewSet, CarViewSet, \
    CarBrandViewSet, CarModelViewSet
from src.customer.views import CustomerViewSet

router = routers.SimpleRouter()
router.register(r'carshowrooms', CarShowroomViewSet)
router.register(r'carspresence', CarShowroomPresenceViewSet)
router.register(r'carsells', CarSellsViewSet)
router.register(r'carbuyers', CarBuyersViewSet)
router.register(r'showroomsales', CarShowroomSalesViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'supplierpresence', SupplierPresenceViewSet)
router.register(r'suppliersales', SupplierSalesViewSet)
router.register(r'cars', CarViewSet)
router.register(r'carbrands', CarBrandViewSet)
router.register(r'carmodels', CarModelViewSet)
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
