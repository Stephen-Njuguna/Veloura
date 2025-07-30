from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Vendor, Customer

#User modification to include emails 

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ("username","email","password1","password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
#subscription form

class SubscriptionForm(forms.Form):
    user_name = forms.CharField(label= 'User Name')
    email = forms.EmailField(label='Email')

# class CustomerCreationForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = '__all__'


# class VendorCreationForm(forms.ModelForm):
#     class Meta:
#         model = Vendor
#         fields = '__all__'