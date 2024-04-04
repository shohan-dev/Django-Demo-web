from django.db import models
import uuid

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True



class Test_Product_1(BaseModel):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    discount = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Test_Product_2(BaseModel):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()  
    add_cart = models.BooleanField(default=False)
    discount = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
