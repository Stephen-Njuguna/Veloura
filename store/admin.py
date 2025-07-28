from django.contrib import admin
from .models import Product,Store,Vendor,Customer
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class VendorAdmin(admin.ModelAdmin):
    list_display = ['vendor','store_name','joined_at']
    list_filter = ['joined_at']
    search_fields = ['phone']

# User admin
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )


#registerinng the models

admin.site.register(Vendor,VendorAdmin)
admin.site.register(Product)
admin.site.register(Store)
admin.site.register(Customer)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)