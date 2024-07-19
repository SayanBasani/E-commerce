from django.urls import path
# from . import views
from customer import views
app_name='customer'
urlpatterns=[
    path("user_login/",views.user_login,name='user_login'),
    path('logOutCustomer/',views.logOutCustomer,name='logOutCustomer'),
    path("Singup/",views.Singup,name='Singup'),
    path("cart/",views.Cart,name='cart'),
    path("remove_item_from_cart/",views.remove_item_from_cart,name='remove_item_from_cart'),
    path("allOrders/",views.allOrders,name='allOrders'),
    path("aboutOrder/",views.aboutOrder,name='aboutOrder'),
    path("place_order/",views.place_order,name='place_order'),
    path("order_place_sucessfull/",views.order_place_sucessfull,name='order_place_sucessfull'),
    
]