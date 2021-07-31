from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    return render(request,'index.html')

def studentspace(request):
    if not request.session.get('user'):
        return HttpResponseRedirect("/login.html")
    return render(request,'studentspace.html')

def teacherspace(request):
    if not request.session.get('user'):
        return HttpResponseRedirect("/teacherlogin.html")
    return render(request,'teacherspace.html')


def hodspace(request):
    if not request.session.get('user'):
        return HttpResponseRedirect("/teacherlogin.html")
    return render(request,'hodspace.html')