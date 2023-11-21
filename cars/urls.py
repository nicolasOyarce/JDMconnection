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
    path('shoppingCart/', views.shopping_cart, name='shopping_cart'),
    path('crudCars/', views.crud_cars, name='crud_cars'),
    path('crudUser/', views.crud_user, name='crud_user'),
    path('add/<int:car_id>/', views.shopping_cart_add, name='shopping_cart_add'),
    path('remove/<int:car_id>/', views.shopping_cart_remove, name='shopping_cart_remove'),
    path('decrement/<int:car_id>/', views.shopping_cart_decrement, name='shopping_cart_decrement'),
    path('clear/', views.shopping_cart_clear, name='shopping_cart_clear'),
    path('', views.process_sale, name='process_sale'),
    path('delete_car/<int:car_id>/', views.delete_car, name='delete_car'),
    path('update_car/<int:car_id>/', views.update_car, name='update_car')
]


