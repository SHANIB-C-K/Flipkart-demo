from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import BookingForm

from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products}) 
    
def buy(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'conformation.html')
    form = BookingForm()
    dict_form={
        'form': form
    }
    return render(request, 'buy.html', dict_form)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username Already Exist')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('login')

    else:
        return render(request, 'register.html')
    
    
def logout(request):
    auth.logout(request)
    return redirect('/')