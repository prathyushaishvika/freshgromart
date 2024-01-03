from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.TextField(db_column='name',null=True)
    number=models.PositiveIntegerField(db_column='number',null=True)
    email=models.TextField(db_column='email',null=True)
    password=models.TextField(db_column='password',null=True)


    class Meta:
        db_table='customer_signin'
