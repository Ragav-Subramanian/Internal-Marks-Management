from django.urls import path

from . import views

urlpatterns = [
    path('login.html', views.Login, name="login"),
    path('teacherlogin.html', views.teacherLogin, name="teacherlogin"),
    path('signup.html', views.Register, name="register"),
    path('teachersignup.html', views.tRegister, name="tregister"),
    path('logout',views.Logout,name="logout")
]