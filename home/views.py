from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from cart.cart import Cart

def index(request):
    cart=Cart(request)
    print(cart)
    return render(request, 'home/home.html')




# def login_post(req)
