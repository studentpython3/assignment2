from django.db import models

# Create your models here.
class user(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    
    email=models.CharField(max_length=100)
    password1=models.CharField(max_length=20)
    password2=models.CharField(max_length=20)
