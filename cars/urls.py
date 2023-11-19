from django.urls import path
from cars import views

urlpatterns = [
    path('', views.index, name="index"),
    path('products/', views.products, name='products'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('products/register/', views.register_car, name='register_car'),
    path('item/<int:car_id>/', views.item, name='item'), 
    path('update/<int:car_id>/', views.update, name='update'), 
    path('about/', views.about, name='about'),
    path('delete/inf:car_id>/', views.delete, name='delete'),
    path('shoppingCart/', views.shopping_cart, name='shopping_cart'),
    path('crudCars/', views.crud_cars, name='crud_cars'),
    path('crudUser/', views.crud_user, name='crud_user'),
]


