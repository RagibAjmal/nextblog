from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def views(request):
    return HttpResponse('user')

def login(request):
    user = authenticate(username='ragibajmal', password='sample111')
    if user is not None:  
        auth_login(request, user)  
        return HttpResponse('Logged in ',user)
    else:   
        return HttpResponse('Login failed')

def logout(request):
    auth_logout(request)  
    return HttpResponse('Logout sucessfully')  
        