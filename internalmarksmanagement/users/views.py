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
        user.password = request.POST.get('password')
        user.batch = request.POST.get('year')
        user.department = request.POST.get('dept')
        user.registerNumber = request.POST.get('regnum')
        user.role = 'Student'
        user.save()
        return HttpResponseRedirect("/login.html")
    return render(request, "signup.html")

def tRegister(request):
    if request.method == "POST":
        print(request.POST)
        user = User()
        user.name = request.POST.get('email') + "teacher"
        user.email = request.POST.get('email')
        user.password = request.POST.get('password')
        user.batch = '1'
        user.department = request.POST.get('dept')
        user.registerNumber = '1'
        user.role = 'Teacher'
        user.save()
        return HttpResponseRedirect("/teacherlogin.html")
    return render(request, "teachersignup.html")

def Login(request):
    if request.method == "POST":
        print(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        be = PersonalizedLoginBackend()
        user = be.authenticate(request, email, password)
        user.save()
        if not user:
            return render(request, "login.html", {"email": email})
        else:
            login(request, user, backend='backends.PersonalizedLoginBackend')
            request.session['logged']=True
            request.session['user'] = {'id':user.uid,'regnum':user.registerNumber,'name':user.name,'email':user.email,'role':user.role}
            return HttpResponseRedirect("/studentspace.html")
    return render(request, "login.html")

def teacherLogin(request):
    if request.method == "POST":
        print(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        be = PersonalizedLoginBackend()
        user = be.authenticate(request, email, password)
        user.save()
        if not user:
            return render(request, "teacherlogin.html", {"email": email})
        else:
            login(request, user, backend='backends.PersonalizedLoginBackend')
            request.session['logged']=True
            request.session['user'] = {'id':user.uid,'regnum':user.registerNumber,'name':user.name,'email':user.email,'role':user.role}
            if user.role=="HOD":
                return HttpResponseRedirect("/hodspace.html")
            return HttpResponseRedirect("/teacherspace.html")
    return render(request, "teacherlogin.html")
