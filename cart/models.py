from django.db import models

from shop.models import *



class Cartlist(models.Model):
    cart_id=models.CharField(max_length=100,unique=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class items(models.Model):
    prodt=models.ForeignKey(products,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cartlist,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.prodt

    def total(self):
        return self.prodt.price*self.quantity