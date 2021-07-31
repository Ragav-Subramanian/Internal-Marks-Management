from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Marks
from users.models import User
from django.db.models import Q
# Create your views here.
def results(request):
    if not request.session.get('user'):
        return HttpResponseRedirect("/login.html")
    print(request.session.get('user').get('email'))
    result =  Marks.objects.filter(Q(email=request.session.get('user').get('email')))
    finalresult = []
    for i in result:
        finalresult.append({'subject':i.subject,i.exam:i.mark})
    print(finalresult)
    return render(request,"semres.html",{"user":request.session.get('user'),"results":finalresult})
def uploadmarks(request):
    if not request.session.get('user'):
        return HttpResponseRedirect("/teacherlogin.html")
    return render(request,"uploadmarks.html")
def unittest(request):
    if not request.session.get('user'):
        return HttpResponseRedirect("/teacherlogin.html")
    if request.method == "POST":
        print(request.POST)
        for subject in ['HS8151','MA8151','PH8151','CY8151','GE8152','GE8151']:    
            user = Marks()
            user.email = User.objects.get(registerNumber=request.POST.get('regnum')).email
            user.exam = 'ut1'
            user.subject = subject
            user.mark = request.POST.get(subject)
            user.save()
            return HttpResponseRedirect("/uploadmarks.html")
    return render(request,"unittest.html")