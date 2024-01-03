from django.db import models
from products.models import Addproducts

# Create your models here.
class Cart(models.Model):
    product=models.ForeignKey(Addproducts,on_delete=models.CASCADE,null=True)
    quantity=models.PositiveIntegerField(default=1)
