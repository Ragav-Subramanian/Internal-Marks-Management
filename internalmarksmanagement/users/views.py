from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from backends import PersonalizedLoginBackend
from .models import User
from passlib.hash import pbkdf2_sha256

def Logout(request):
    if not request.session.get('user'):
        return HttpResponseRedirect("/login.html")
    user = User.objects.get(uid=int(request.session['user']['id']))
    user.is_active=0
    user.save()
    logout(request)
    return HttpResponseRedirect('/login.html')


def Register(request):
    if request.method == "POST":
        print(request.POST)
        user = User()
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.password = pbkdf2_sha256.encrypt(request.POST.get('password'),rounds=12000,salt_size=32)
        user.batch = request.POST.get('year')
        user.department = request.POST.get('dept')
        user.registerNumber = request.POST.get('regnum')
        user.role = 'Student'
        user.save()
        return HttpResponseRedirect("/login.html")
    return render(request, "signup.html")


def Login(request):
    if request.method == "POST":
        print(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        be = PersonalizedLoginBackend()
        user = be.authenticate(request, email, password)
        user.is_active=1
        user.save()
        if not user:
            return render(request, "login.html", {"email": email})
        else:
            login(request, user, backend='backends.PersonalizedLoginBackend')
            request.session['logged']=True
            request.session['user'] = {'id':user.uid,'regnum':user.registerNumber,'name':user.name,'email':user.email,'role':user.role}
            return HttpResponseRedirect("/dashboard.html")
    return render(request, "login.html")
