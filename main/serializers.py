from rest_framework import serializers, viewsets

from main.models import ColorTone, Industry, Logo, Services, SubProduct, Product, TypeAndPreferences


class ColorToneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorTone
        fields = '__all__'


class IndustriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'


class LogoSerializer(serializers.ModelSerializer):
    # industry = IndustriesSerializer(many=True)
    # color_tone = ColorToneSerializer(many=True)
    class Meta:
        model = Logo
        fields = ['business_name', 'email', 'user_name', 'slogan', 'industry', 'color_tone', 'type_and_preferences']
        extra_kwargs = {'business_name': {'required': True},
                        'slogan': {'required': False},
                        'color_tone': {'required': False},
                        'industry': {'required': False},
                        'type_and_preferences': {'required': False},
                        'email': {'required': True},
                        'user_name': {'required': True},
                        }

class ServiceSerializer(serializers.ModelSerializer):
    # sub_product = SubProductSerializer(many=False)
    class Meta:
        model = Services
        fields = '__all__'


class SubProductSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True)

    class Meta:
        model = SubProduct
        fields = ['title', 'price', 'image', 'services']


class ProductSerializer(serializers.ModelSerializer):
    sub_products = SubProductSerializer(many=True)

    class Meta:
        model = Product
        fields = ['price', 'title', 'sub_products']


class PreferencesSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeAndPreferences
        fields = '__all__'
