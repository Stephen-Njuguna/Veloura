from rest_framework import serializers
from .models import Vendor,Customer,Product,Store

#Define serilazation for all models

class Vendorserializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

#Customer Serializer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

#product Serializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

#Store serializer

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model =Store
        fields = '__all__'