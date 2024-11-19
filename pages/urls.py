from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('location', LocationViewSet)
router.register('category', CategoryViewSet)
router.register('menu', MenuViewSet)
router.register('address', AddressViewSet)
router.register('onlocation', OnLocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]