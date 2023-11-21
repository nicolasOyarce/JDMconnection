from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.db.models import F, Sum, FloatField

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
    price       = models.FloatField()
    register    = models.DateTimeField(auto_now_add=True)
    image       = models.ImageField(upload_to="cars_img", null=True)

    def __str__(self):
        return self.brand + ' ' + self.model + ' ' + self.age


class Sale(models.Model):

    folio     = models.CharField(max_length=6, primary_key=True, auto_created=True)
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    register  = models.DateTimeField(auto_now_add=True)


    def __init__(self):
        return self.folio
    
    @property
    def total(self):
        return self.salesdatail_set.aggregate(
            
            total = Sum(F("price")*F("quantity"), output_field = FloatField())
        )["total"]
    
    class Meta:

        db_table = 'sale'
        ordering = ['folio']


class SalesDetail(models.Model):

    folio      = models.ForeignKey(Sale, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Cars, on_delete=models.CASCADE)
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity   = models.IntegerField(default=1, null=False)
    register  = models.DateTimeField(auto_now_add=True)

    def __init__(self):
        return self.user + ' ' + self.quantity
    
    class Meta:

        db_table = 'saledetail'
        ordering = ['id']