from rest_framework import serializers
from .models import Vendor,Customer,Product,Store
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

#Define serilazation for all models
#user serializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password_confirmation"]

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError("Passwords do not match")
        validate_password(data['password'])
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
#Vendor serializer
class Vendorserializer(serializers.ModelSerializer):
    vendor = UserSerializer()
    class Meta:
        model = Vendor
        fields = ['vendor', 'store_name', 'bio', 'phone']

    def create(self, validated_data):
        user_data = validated_data.pop('vendor')
        user = UserSerializer().create(user_data)
        vendor = Vendor.objects.create(vendor=user, **validated_data)
        return vendor


#Customer Serializer

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Customer
        fields = ['user','phone_no']

    def create(self, validated_data):
        # Take user part out
        user_data = validated_data.pop('user')
        # Create user first
        user = UserSerializer().create(user_data)
        # Then create customer and link to user
        customer = Customer.objects.create(user=user, **validated_data)
        return customer


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

