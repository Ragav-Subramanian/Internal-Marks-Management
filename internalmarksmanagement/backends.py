from django.contrib.auth.backends import ModelBackend
from users.models import User
from django.contrib.auth.hashers import *


class PersonalizedLoginBackend(ModelBackend):
    def authenticate(self, request=None, email=None, password=None, **kwars):
        # Here define you login criteria, like encrypting the password and then
        # Checking it matches. This is an example:
        try:
            user = User.objects.get(email=email)
            print(user.password,password,email,request.POST)
        except User.DoesNotExist:
            return None
        if user.password==password:
            return user
        else:
            return None

    def get_user(self, user_id):
        # This shall return the user given the id
        try:
            user = User.objects.get(uid=user_id)
        except Exception:
            user = None
        return user