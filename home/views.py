from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, 'home/home.html')




# def login_post(req)
