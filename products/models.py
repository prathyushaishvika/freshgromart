from django.db import models

# Create your models here.
class Category(models.Model):
    c_name=models.TextField(max_length=50,null=True)
    c_image=models.ImageField(upload_to='images',blank=True,null=True)
    def __str__(self):
        return self.c_name


class Addproducts(models.Model):
    name=models.TextField(max_length=100,null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    img=models.ImageField(upload_to='images',null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    status=models.TextField(null=True)
    def __str__(self):
        return self.name

    class Meta:
        db_table='product_items'

class Addvegetables(models.Model):
    name=models.TextField(max_length=100,null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    img=models.ImageField(upload_to='images',null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    status=models.TextField(null=True)

    class Meta:
        db_table='vegetable_items'

class Addbackery(models.Model):
    name=models.TextField(max_length=100,null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    img=models.ImageField(upload_to='images',null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    status=models.TextField(null=True)

    class Meta:
        db_table='backery_items'

class Addfoodgrain(models.Model):
    name=models.TextField(max_length=100,null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    img=models.ImageField(upload_to='images',null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    status=models.TextField(null=True)

    class Meta:
        db_table='foodgrain_items'
    