from django.db import models

# Create your models here.


class personal(models.Model):
    username = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)
    phone = models.PositiveBigIntegerField(unique=True)
    password = models.CharField(max_length=30)
    repassword = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, choices=[
                              ['male', 'Male'], ['female', 'Female']])
    dob = models.DateField()
    dor = models.DateTimeField(auto_now_add=True)
