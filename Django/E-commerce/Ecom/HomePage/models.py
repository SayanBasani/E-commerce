from django.db import models

# Create your models here.
class cart(models.Model):
    customer_id =   models.CharField(max_length=20)
    productId =     models.CharField(max_length=20)
    quentity =      models.CharField(max_length=10)
    Time      =     models.CharField(max_length=30)