from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('HomePage.url')),
    # path('HomePage/',include('HomePage.url')),
    path('Sell/',include('Seller.url')),
    path('customer/',include('customer.url')),
]
