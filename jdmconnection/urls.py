from django.contrib import admin
from django.urls import path
from cars import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('products/', views.products, name='products'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('products/register/', views.register_car, name='register_car'),
    path('item/', views.item, name='item'), #<str:codigo>/
    path('update/', views.update, name='update'), #<str:car_codigo>/
    path('about/', views.about, name='about'),
    path('delete/', views.delete, name='delete'), #<str:car_codigo>/
    path('shoppingCart/', views.shopping_cart, name='shopping_cart'),
    path('crudCars/', views.crud_cars, name='crud_cars'),
    path('crudUser/', views.crud_user, name='crud_user'),
]

