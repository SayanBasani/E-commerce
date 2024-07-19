from django.db import models

class user_singup(models.Model):
    Name = models.CharField(max_length=50)
    Mobile_number = models.CharField(max_length=50)
    Email = models.CharField(max_length=50,primary_key=True)
    password = models.CharField(max_length=20)
    main_id = models.CharField(max_length=20)
    Type = models.CharField(max_length=20 , default='Customer')

    # def __str__(self):
    #     return self.Name
class shoppingAddres(models.Model):
    customerId =            models.CharField(max_length=50,null=False)
    ReciverName =           models.CharField(max_length=60,null=False)
    ReciverMobileNo =       models.CharField(max_length=15,null=False)
    state =                 models.CharField(max_length=50,null=False)
    city =                  models.CharField(max_length=50,null=False)
    pincode =               models.CharField(max_length=10,null=False)
    Home_Rode_Address =     models.CharField(max_length=150,null=False)
    def __str__(self):
        return f'{self.customerId},{self.ReciverName},{self.ReciverMobileNo},{self.state},{self.city},{self.pincode},{self.Home_Rode_Address}'
class orders(models.Model):
    customer_id =           models.CharField(max_length=20)
    customer_address =      models.CharField(max_length=1000)
    productId =             models.CharField(max_length=20)
    quentity =              models.CharField(max_length=10)
    Time      =             models.CharField(max_length=30)
    ReciverName =           models.CharField(max_length=60,null=False)
    ReciverMobileNo =       models.CharField(max_length=15,null=False)
    state =                 models.CharField(max_length=50,null=False)
    city =                  models.CharField(max_length=50,null=False)
    pincode =               models.CharField(max_length=10,null=False)
    Home_Rode_Address =     models.CharField(max_length=150,null=False)
    def __str__(self):
        return f'{self.customer_id},{self.customer_address},{self.productId},{self.quentity},{self.Time},{self.ReciverName},{self.ReciverMobileNo},{self.state},{self.city},{self.pincode},{self.Home_Rode_Address}'