from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductDetails, ProductListCreate,StoreDetails,StoreCreate,RegisterCustomer,RegisterVendor,LoginAPI,LogoutAPI

urlpatterns = [
    path('products/', ProductListCreate.as_view()),
    path('products/<int:pk>/', ProductDetails.as_view()),
    path('stores/',StoreCreate.as_view()),
    path('stores/<slug:slug>/products',StoreDetails.as_view()),
    path('login/',LoginAPI.as_view()),
    path('logout/',LogoutAPI.as_view()),
    path('register/vendor/', RegisterVendor.as_view(), name='register_vendor'),
    path('register/customer/', RegisterCustomer.as_view(), name='register_customer'),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)