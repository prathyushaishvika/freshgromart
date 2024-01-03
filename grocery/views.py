from django.shortcuts import render,redirect
from.models import *
from django.http import JsonResponse


# from .forms import ProductForm

 

# Create your views here.


def viewproduct(request):
    return render(request,'grocery/viewproduct.html')


def dashboard(request):
    return render(request,'grocery/dashboard.html')

def manageorder(request):
    return render(request,'grocery/manageorder.html')



def adminmaster(request):
    return render(request,'grocery/adminmaster.html')

def admindashboard(request):
    return render(request,'grocery/admindashboard.html')

def adminhome(request):
    return render(request,'grocery/adminhome.html')


def adminsignup(request):
    if request.method=='POST':
        name=request.POST['name']
        number=request.POST['number']
        email=request.POST['email']
        password=request.POST['password']

        grocery=Grocery(name=name,email=email,number=number,password=password)
        grocery.save()
    return render(request,'grocery/adminsignup.html')

def adminlogin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        if Grocery.objects.filter(email=email,password=password).exists():
             return redirect('groceryadmin:adminhome')
        
        else:

            return render(request,'grocery/adminlogin.html')
    return render(request,'grocery/adminlogin.html')
    
        
    



def additem(request):
        if request.method=='POST':
           title=request.POST['title']
           amount=request.POST['amount']
           picture=request.POST['picture']
           brief=request.POST['brief']  
           items=AddItems(title=title,picture=picture,amount=amount,brief=brief)
           items.save()
           return redirect('groceryadmin:admindashboard')  
        
        return render(request,'grocery/additem.html')     
        

          
