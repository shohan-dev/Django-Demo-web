from django.db import models

# Create your models here.


    

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField()
    file = models.FileField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField()
    file = models.FileField()
