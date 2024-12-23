from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import OnLocationSerializer
from .models import OnLocation
from django.shortcuts import render, redirect, get_object_or_404

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
    queryset = Menu.objects.all().order_by('menu_position')  # Order by menu_position
    serializer_class = MenuSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class OnLocationViewSet(viewsets.ModelViewSet):
    queryset = OnLocation.objects.all()
    serializer_class = OnLocationSerializer

