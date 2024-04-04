from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField()
    file = models.FileField()

    def __str__(self):
        return self.name
    

# signal handlers to find the changes in the database
@receiver(pre_save, sender=Product)
def print_status(sender, instance, **kwargs):
    if instance.id:
        old_name = sender.objects.get(id=instance.id).name
        new_name = instance.name
        print("Old Name:", old_name)
        print("New Name:", new_name)
