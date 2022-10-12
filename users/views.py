from django import http
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import User

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
            return redirect('/user')
        else:
            return HttpResponse('로그인 실패')

            