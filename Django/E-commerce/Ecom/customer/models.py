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
