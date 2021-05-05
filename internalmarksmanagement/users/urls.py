from django.urls import path

from . import views

urlpatterns = [
    path('login.html', views.Login, name="login"),
    path('signup.html', views.Register, name="register"),
    path('logout',views.Logout,name="logout")
]