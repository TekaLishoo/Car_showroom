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

from config import settings
from src.carshowroom.views import (
    CarShowroomViewSet,
    CarShowroomPresenceViewSet,
    CarSellsViewSet,
    CarBuyersViewSet,
    CarShowroomSalesViewSet,
)
from src.supplier.views import (
    SupplierViewSet,
    SupplierPresenceViewSet,
    SupplierSalesViewSet,
    CarViewSet,
    CarBrandViewSet,
    CarModelViewSet,
)
from src.customer.views import CustomerViewSet, CustomerOfferViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_swagger.views import get_swagger_view  # noqa F401
from rest_framework.schemas import get_schema_view

from rest_framework.renderers import CoreJSONRenderer

schema_view = get_schema_view(
    title="A Different API", renderer_classes=[CoreJSONRenderer]
)

router = routers.SimpleRouter()
router.register(r"carshowrooms", CarShowroomViewSet)
router.register(r"carspresence", CarShowroomPresenceViewSet)
router.register(r"carsells", CarSellsViewSet)
router.register(r"carbuyers", CarBuyersViewSet)
router.register(r"showroomsales", CarShowroomSalesViewSet)
router.register(r"suppliers", SupplierViewSet)
router.register(r"supplierpresence", SupplierPresenceViewSet)
router.register(r"suppliersales", SupplierSalesViewSet)
router.register(r"cars", CarViewSet)
router.register(r"carbrands", CarBrandViewSet)
router.register(r"carmodels", CarModelViewSet)
router.register(r"customers", CustomerViewSet)
router.register(r"customeroffers", CustomerOfferViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("swagger/", schema_view),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
