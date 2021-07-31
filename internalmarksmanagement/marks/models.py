from django.db import models

# Create your models here.
class Marks(models.Model):
    email = models.EmailField(max_length=80)
    exam = models.TextField()
    subject = models.TextField()
    mark = models.IntegerField()