from django.shortcuts import render,redirect
from .serializers import ProductSerializer, Vendorserializer,CustomerSerializer,StoreSerializer
from .forms import SubscriptionForm
from .models import Store,Product,Customer,Vendor
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token

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
class StoreCreate(APIView):
    def get(self, request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StoreSerializer(data=request.data)
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
        products = Product.objects.filter(vendor=store.vendor)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
#vendor post

class RegisterVendor(APIView):
    
    def post(self, request):
        serializer = Vendorserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Vendor created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterCustomer(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Customer created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Login Request 
class LoginAPI(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user) 
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        
        return Response({'message': 'Username or password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)
    
#logout request
class LogoutAPI(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)

    
#Token class
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = token.user
        return Response({
            'token': token.key,
            'user_id': user.id,
            'username': user.username,
        })
