from django.db import models
from django.contrib.auth.models import User

# Models

class Cars(models.Model):

    brand       = models.CharField(max_length=30)
    model       = models.CharField(max_length=50)
    color       = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    type_car    = models.CharField(max_length=30)
    age         = models.CharField(max_length=4)
    used        = models.BooleanField(default=True)
    count       = models.IntegerField(default=1, null=False)
    price       = models.CharField(max_length=20)
    register    = models.DateTimeField(auto_now_add=True)
    image       = models.ImageField(upload_to="cars_img", null=True)
    #user        = models.models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.brand + ' ' + self.model + ' ' + self.age
