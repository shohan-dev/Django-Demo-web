from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    image = models.ImageField(upload_to='img/')  # Specify the 'upload_to' parameter
