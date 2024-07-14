from django.urls import path
# from . import views
from customer import views
app_name='customer'
urlpatterns=[
    path("user_login/",views.user_login,name='user_login'),
    path('logOutCustomer/',views.logOutCustomer,name='logOutCustomer'),
    path("Singup/",views.Singup,name='Singup'),
    path("cart/",views.cart,name='cart'),
    path("order/",views.order,name='order'),
    path("product_list/",views.product_list,name='product_list'),
    
]