from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CarsForm
from .models import Cars, Sale, SalesDetail
from django.contrib.auth.decorators import login_required
from .cart import ShoppingCart
from django.contrib import messages
# Create your views here.

# View in charge of displaying the index data
def index(request):

    cars = Cars.objects.all()
    cars_index = cars[:8]

    return render(request, "index.html", {
        'cars': cars_index
    })


# Session startup view
def signin(request):

    if request.method == 'GET':

        return render(request, 'login/signin.html', {
            'form': AuthenticationForm
        })

    else:

        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'login/signin.html', {
                'form': AuthenticationForm,
                'error': 'Nombre de usuario o contrasena incorrecta'
            })

        else:

            login(request, user)
            return redirect('index')


# View to logout
@login_required
def signout(request):

    logout(request)
    return redirect('index')



def signup(request):

    if request.method == 'GET':

        return render(request, 'login/signup.html', {
            'form': UserCreationForm
        })

    else:

        if request.POST['password1'] == request.POST['password2']:

            try:
                # Register User
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)

                return redirect('index')

            except IntegrityError:
                # Failed Register
                return render(request, 'login/signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })

        return render(request, 'login/signup.html', {
            'form': UserCreationForm,
            'error': 'Las contrasenas no coinciden'
        })



#
def register_car(request):
    if request.method == 'GET':
        return render(request, "crud/register_car.html", {'form': CarsForm})

    else:
        try:
            form = CarsForm(request.POST, request.FILES)
            if form.is_valid():
                new_car = form.save(commit=False)
                new_car.image = request.FILES.get('txtImagen')
                new_car.save()
                return redirect('products')
            else:
                # Handle form validation errors
                return render(request, 'crud/register_car.html', {'form': form, 'error': 'Ingresa datos válidos'})
        except Exception as e:
            # Handle other exceptions
            return render(request, 'crud/register_car.html', {'form': CarsForm, 'error': 'Error: {}'.format(str(e))})


def item(request, car_id):
    
    car = get_object_or_404(Cars, pk = car_id)
    return render(request, "crud/item.html", {
        'car': car
    })


#
@login_required
def update(request, car_id):

    if request.method == 'GET':

        car = get_object_or_404(Cars, pk = car_id)
        form = CarsForm(instance=car)
        return render(request, "crud/update.html", {
            'car': car,
            'form': form
        })
    
    else:

        try:
            car = get_object_or_404(Cars, pk = car_id)
            form = CarsForm(request.POST, instance = car)
            form.save()

            return redirect('crud/crud_cars')
        
        except ValueError:

            return render(request, "update.html", {
                'car': car,
                'form': form,
                'error': "Error al actualizar"
            })


@login_required
def delete_car(request, car_id):
    car = get_object_or_404(Cars, id=car_id)
    car.delete()
    return redirect('crud_cars')  # Cambia 'products' con la URL a la que deseas redirigir después de eliminar

def update_car(request, car_id):
    car = get_object_or_404(Cars, id=car_id)
    
    if request.method == 'POST':
        form = CarsForm(request.POST, request.FILES, instance=car)
        
        if form.is_valid():

            car.image.delete(save=False)
            car = form.save(commit=False)
            car.image = request.FILES.get('txtImagen')
            form.save()
            return redirect('products')


    else:
        form = CarsForm(instance=car)

    return render(request, 'crud/update_car.html', {'form': form})

def products(request):

    cars = Cars.objects.all()
    return render(request, "crud/products.html", {
        'cars': cars
    })


def about(request):
    return render(request, "about.html")



# SHOPPING CART
## View
def shopping_cart(request):
    return render(request, 'buy/shopping_cart.html')

## Add
def shopping_cart_add(request, car_id):

    cart = ShoppingCart(request)
    product = Cars.objects.get(id=car_id)
    
    cart.add(product=product)

    return redirect('shopping_cart')
    
## Remove
def shopping_cart_remove(request, car_id):

    cart = ShoppingCart(request)
    product = Cars.objects.get(id=car_id)
    
    cart.remove(product=product)

    return redirect('shopping_cart')

## Decrement 
def shopping_cart_decrement(request, car_id):

    cart = ShoppingCart(request)
    product = Cars.objects.get(id=car_id)
    
    cart.decrement(product=product)

    return redirect('shopping_cart')

## Clear 
def shopping_cart_clear(request):

    cart = ShoppingCart(request)
    
    cart.clear()

    return redirect('shopping_cart')









# Cruds
@login_required
def crud_cars(request):

    cars = Cars.objects.all()
    return render(request, "crud/crud_cars.html", {
        'cars': cars
    })

@login_required
def crud_user(request):

    users = User.objects.all()




    return render(request, "crud/crud_user.html", {
        'users': users,
    })


#
@login_required
def process_sale(request):
    
    order = Sale.objects.create(user = request.user)
    cart = ShoppingCart(request)
    items_cart = list()

    for key, value in cart.cart.items():
        items_cart.append(SalesDetail(

            product_id = key,
            quantity = value["quantity"],
            user = request.user,
            order = order
        ))

    SalesDetail.objects.bulk_create(items_cart)

    messages.success(request, "El pedido se ha creado correctamente")

    return redirect('index')