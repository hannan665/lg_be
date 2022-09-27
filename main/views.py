from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from main.models import ColorTone, Industry, Logo, Product, TypeAndPreferences
from main.serializers import ColorToneSerializer, IndustriesSerializer, LogoSerializer, ProductSerializer, \
    PreferencesSerializer


# Create your views here.

class GetColorTones(ModelViewSet):
    serializer_class = ColorToneSerializer
    queryset = ColorTone.objects.all()
    # http_method_names = ['get', 'head']


class GetIndustries(ModelViewSet):
    serializer_class = IndustriesSerializer
    queryset = Industry.objects.all()
    http_method_names = ['get', 'head']


class CreateLogo(ModelViewSet):
    serializer_class = LogoSerializer
    queryset = Logo.objects.all()
    http_method_names = ['post', 'head']

    # def perform_create(self, serializer):
    #     if serializer.is_valid():
    #         serializer.save()


class GetProducts(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    http_method_names = ['get', 'head']



class GetPreferences(ModelViewSet):
    serializer_class = PreferencesSerializer
    queryset = TypeAndPreferences.objects.all()
    http_method_names = ['get', 'head']


