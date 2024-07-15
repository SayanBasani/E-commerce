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
class addShoppingAddres(models.Model):
    customerId = models.CharField(max_length=30,null=False)
    ReciverName = models.CharField(max_length=50,null=False)
    ReciverMobileNo = models.CharField(max_length=30,null=False)
    state = models.CharField(max_length=30,null=False)
    city = models.CharField(max_length=30,null=False)
    pincode = models.CharField(max_length=20,null=False)
    Home_Rode_Address = models.CharField(max_length=150,null=False)
    