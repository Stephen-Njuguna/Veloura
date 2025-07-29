from django.shortcuts import render,redirect
from .serializers import ProductSerializer, Vendorserializer,CustomerSerializer,StoreSerializer
from .forms import SubscriptionForm,CustomUserCreationForm
from .models import Store,Product,Customer,Vendor
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from rest_framework import status
# Create your views here.

#Product post and get 

class ProductListCreate(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#product details patch,delete

class ProductDetails(APIView):
    def get( self, request, pk):
        product = Product.objects.get(pk =pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def patch(self, request,pk):
        product = Product.objects.get(pk =pk)
        serializer = ProductSerializer(product, data =request.data, partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        product = Product.objects.get(pk =pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#Store post
class StoreList(APIView):
    def post(self, request)
        serializer = StoreSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#store details 

class StoreDetails(APIView):
    def patch(self, request,slug):
        store = Store.objects.get(store_name = slug)
        serializer = StoreSerializer(store, data =request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,slug):
        store = Store.objects.get(store_name = slug)
        Product = Product.objects.filter(vendor = store.vendor)
        serializer = ProductSerializer(Product, many=True)
        return Response(serializer.data)
    
#vendor post

class VendorList(APIView):
    def post(self, request):
        serializer = Vendorserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
