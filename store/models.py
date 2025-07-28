from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

# Create your models here.
#Vendor & customer groups
class UserType(models.TextChoices):
    CUSTOMER = 'customer', 'Customer'
    VENDOR = 'vendor', 'Vendor'
   


#creating vendor model
class Vendor(models.Model):
    vendor = models.OneToOneField(User, on_delete=models.CASCADE)
    store_name = models.SlugField(max_length=100, unique=True)
    bio = models.TextField(blank=True)
    joined_at = models.DateField(auto_now_add=True)
    phone = models.CharField(max_length=10, blank=True)
    user_type = models.CharField(choices=UserType.choices, default=UserType.VENDOR)

    def __str__(self):
        return self.vendor.username
    
#product status

class ProductChoices(models.TextChoices):
    SOLD = 'sold', 'Sold'
    AVAILABLE = 'available', 'Available'
    RESERVED_ONLINE = 'reserved-online', 'Reserved Online'

#Products model
class Product(models.Model):
    vendor  = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to='products/', blank=False)
    status = models.CharField(max_length=30, choices=ProductChoices.choices, default=ProductChoices.AVAILABLE)
    added_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    

#Store model

class Store(models.Model):
    Vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    store_name = models.SlugField(unique=True,blank=False)
    banner = models.ImageField(upload_to='banners/', blank=True)
    joined_on = models.DateField(auto_now_add=True)
    location = models.TextField()

    def __str__(self):
        return self.store_name
    
    #return products sold by same vendor

    def get_products(self):
        return Product.objects.filter(vendor=self.vendor)
    
    #Auto fill store name 

    def save(self, *args, **kwargs):
        self.store_name = slugify(self.vendor.store_name)
        super().save(*args, **kwargs)

#Customers model
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=10, unique=True)
    user_type = models.CharField(choices=UserType.choices, default=UserType.CUSTOMER)
    
    def __str__(self):
        return self.user.username
    
