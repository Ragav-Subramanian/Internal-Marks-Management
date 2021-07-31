from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('index.html', views.home, name="home"),
    path('studentspace.html', views.studentspace, name="studentspace"),
    path('teacherspace.html', views.teacherspace, name="teacherspace"),
    path('hodspace.html', views.hodspace, name="hodspace"),
]