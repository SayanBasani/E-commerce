from django.db import models

# Create your models here.
class user_singup(models.Model):
    user_name = models.CharField(max_length=50)
    Mobile_number = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_password = models.CharField(max_length=20)
    user_id = models.CharField(max_length=20)
    def __str__(self):
        return self.user_name