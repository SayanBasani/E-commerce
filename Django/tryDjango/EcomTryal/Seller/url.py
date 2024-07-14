from django.urls import path 
from . import views

app_name='Seller'
urlpatterns = [
    path('',views.sellerHome,name='sellerHome'),
    path('Seller_login/',views.Seller_login,name='Seller_login'),
    path('logout/',views.Seller_login,name='logout'),
    path('Seller_Singup/',views.Seller_Singup,name='Seller_Singup'),
    path('sellerHome/',views.sellerHome,name='sellerHome'),
    path('sellerUplod/',views.sellerUplod,name='sellerUplod'),    
]