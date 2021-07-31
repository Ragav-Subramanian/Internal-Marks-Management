from django.urls import path

from . import views

urlpatterns = [
    path('semres.html', views.results, name="semres"),
    path('uploadmarks.html', views.uploadmarks, name="upmar"),
    path('unittest.html', views.unittest, name="ut"),
]