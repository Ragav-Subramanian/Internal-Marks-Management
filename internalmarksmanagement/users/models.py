from django.db import models
from passlib.hash import pbkdf2_sha256
from django.utils import timezone
# Create your models here.
ROLE_CHOICES = [
    ("Student","Student"),
    ("Teacher","Teacher"),
    ("HOD","HOD"),
    ("admin","admin")
]
class User(models.Model):
    uid = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=80)
    password = models.TextField()
    batch = models.IntegerField(default=0)
    department = models.CharField(default="Computer Science Engineering",max_length=50)
    role = models.CharField(max_length=20,choices=ROLE_CHOICES)
    registerNumber = models.CharField(max_length=25)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)
    
    @property
    def is_authenticated(self):
        return True