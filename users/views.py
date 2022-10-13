from django import http
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import User
from django.contrib.auth import authenticate, login as loginsession

# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        password2 = request.POST.get('passwordcheck','')
        
        if password == password2:       
            User.objects.create_user(username=username, password=password)
            return redirect('users:login')
        else:
            return HttpResponse('로그인 실패')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            loginsession(request, user)
            return redirect('users:user')
        else:
            return HttpResponse('로그인 실패!')


def user(request):
    return HttpResponse(request.user)


def profile(request, username ):
    user = User.objects.get(username=username)
    context = {
        'user':user
    }
    return  render(request, 'profile.html', context)
