from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    return render(request,'index.html')

def dashboard(request):
    if not request.session.get('user'):
        return HttpResponseRedirect("/login.html")
    return render(request,'dashboard.html')