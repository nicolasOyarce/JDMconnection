from django.forms import ModelForm, forms
from .models import Cars

class CarsForm(ModelForm):

    class Meta:
        model = Cars
        fields = ['brand', 'model', 'description', 'price','age','color','type_car']

