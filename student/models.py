from django.contrib.auth.models import User
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField(max_length=100,unique=True)
    phone = models.CharField(max_length=20)
    standard = models.CharField(max_length=20)
    userid = models.OneToOneField(User,on_delete=models.CASCADE,related_name='student_user')
