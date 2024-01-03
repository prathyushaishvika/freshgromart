from django.shortcuts import render
from.models import *


# Create your views here.
def cart(request):
    return render(request,'cart/cart.html')

