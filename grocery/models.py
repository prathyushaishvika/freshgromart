from django.db import models

# Create your models here.

class Grocery(models.Model):
    name=models.TextField(db_column='name',null=True)
    number=models.PositiveIntegerField(db_column='number',null=True)
    email=models.TextField(db_column='email',null=True)
    password=models.TextField(db_column='password',null=True)


    class Meta:
        db_table='grocery_signup'

class AddItems(models.Model):
    title=models.TextField(max_length=100,null=True)
    amount=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    picture=models.ImageField(upload_to='product_images/',null=True,blank=True)
    brief=models.TextField(null=True)

    class Meta:
        db_table='grocery_items'


