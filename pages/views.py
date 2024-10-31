from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request 
        return context



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryRetriveSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer