from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.db.models import F, Sum, FloatField
from django.dispatch import receiver
from django.db.models.signals import pre_save

# Models

class Cars(models.Model):

    brand       = models.CharField(max_length=30)
    model       = models.CharField(max_length=50)
    color       = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    type_car    = models.CharField(max_length=30)
    age         = models.CharField(max_length=4)
    used        = models.BooleanField(default=True)
    stock       = models.IntegerField(default=1, null=False)
    price       = models.IntegerField()
    register    = models.DateTimeField(auto_now_add=True)
    image       = models.ImageField(upload_to="cars_img", null=True)
    in_stock    = models.BooleanField(default=True)

    def __str__(self):
        return self.brand + ' ' + self.model + ' ' + self.age

    class Meta:

        db_table = 'cars'
        ordering = ['id']



@receiver(pre_save, sender=Cars)
def update_in_stock(sender, instance, **kwargs):
    instance.in_stock = instance.stock > 0

class Sale(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    date        = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField(default=0)


    def __str__(self):
        return str(self.user) + " / numero de compra: " + str(self.id)


class SalesDetail(models.Model):
    sale     = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product  = models.ForeignKey(Cars, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price    = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.sale) + " - " + str(self.product)
    
    def total_price(self):
        return self.product.price * self.quantity