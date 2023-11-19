from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CarsForm
from .models import Cars
from django.contrib.auth.decorators import login_required

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

        return render(request, "crud/register_car.html", {
            'form': CarsForm
        })

    else:

        try:
            form = CarsForm(request.POST)
            new_car = form.save(commit=False)
            new_car.save()

            return redirect('products')

        except:
            return render(request, 'crud/register_car.html', {
                'form': CarsForm,
                'error': 'Ingresa datos validos'
            })


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
def delete(request, car_id):

    car = get_object_or_404(Cars, pk = car_id)

    if request.method == 'POST':
        car.delete()

        return redirect('mod_car')


def products(request):

    cars = Cars.objects.all()
    return render(request, "crud/products.html", {
        'cars': cars
    })


def about(request):
    return render(request, "about.html")


def shopping_cart(request):

    cars = Cars.objects.all()
    return render(request, "buy/shopping_cart.html", {
        'cars': cars
    })

@login_required
def crud_cars(request):

    cars = Cars.objects.all()
    return render(request, "crud/crud_cars.html", {
        'cars': cars
    })

@login_required
def crud_user(request):

    users = User.objects.all()

    test = User.objects.get(username='admin')
    permissions_user = test.user_permissions.all()



    return render(request, "crud/crud_user.html", {
        'users': users,
        'aaa': permissions_user
    })