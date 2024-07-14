from django.urls import path
from . import views
app_name='homepage'
urlpatterns = [
    path('',views.HomePage,name='HomePage'),
    path('HomePage/',views.HomePage,name='HomePage'),
    path('product/',views.product,name='product'),
    path('addToCart/',views.addToCart,name='addToCart'),
]