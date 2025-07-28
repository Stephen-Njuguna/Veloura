from django.shortcuts import render,redirect
from .serializers import ProductSerializer, Vendorserializer,CustomerSerializer,StoreSerializer
from .forms import SubscriptionForm,CustomUserCreationForm
from .models import Store,Product,Customer,Vendor
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
