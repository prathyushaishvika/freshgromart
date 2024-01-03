from django.shortcuts import render,redirect,get_object_or_404
from.models import *
from products.models import *
from cart.models import *




# Create your views here.
def indexhome(request):
    return render(request,'customerapp/main.html')

def fruits(request):
    fruit=Category.objects.get(c_name='Fruits')
    pdt=Addproducts.objects.filter(category=fruit)
    return render(request,'customerapp/fruits.html',{'products':pdt})

def main(request):
    return render(request,'customerapp/main.html')

def master(request):
    return render(request,'customerapp/master.html')

def category(request):
    return render(request,'customerapp/category.html')


def vegetables(request):
    vege=Category.objects.get(c_name='vegetables')
    pdts=Addproducts.objects.filter(category=vege)
    return render(request,'customerapp/vegetables.html',{'vegetable':pdts})

def foodgrains(request):
    grain=Category.objects.get(c_name='foodgrains')
    fdgns=Addproducts.objects.filter(category=grain)
    return render(request,'customerapp/foodgrains.html',{'foodgrains':fdgns})

def backery(request):
    backery=Category.objects.get(c_name='Backery')
    bkds=Addproducts.objects.filter(category=backery)
    return render(request,'customerapp/backery.html', {'backery':bkds})

def home(request):
    return render(request,'customerapp/home.html')



def booking(request):
    return render(request,'customerapp/booking.html')

def viewcart(request):
    cart_item=Cart.objects.all()
    # totalprice=sum(item.product.price*item.quantity for item in cart_item)
    return render(request,'customerapp/viewcart.html',{'cart_items':cart_item})

def payment(request):
    return render(request,'customerapp/payment.html')

def changepassword(request):
    return render(request,'customerapp/changepassword.html')


def trackorderstatus(request):
    return render(request,'customerapp/trackorderstatus.html')


def signup(request):
    if request.method=='POST':
        name=request.POST['name']
        number=request.POST['number']
        email=request.POST['email']
        password=request.POST['password']

        customer=Customer(name=name,email=email,number=number,password=password)
        customer.save()
    return render (request,'customerapp/signup.html')

def Login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        try:
            customer=Customer.objects.get(email=email,password=password)
        except Customer.DoesNotExist:
            err='invalid user name or password'
            return render(request,'customerapp/login.html',{'error':err})
        return redirect('customer:main')
        
    return render(request,'customerapp/login.html')

def Dashboard(request):
    return render(request,'customerapp/main.html')



def addtocartf(request,pid):
    if request.method=='POST':
       product=Addproducts.objects.get(id=pid)
       cart_item,created=Cart.objects.get_or_create(product=product)
       if not created:
           cart_item.quantity+=1
           cart_item.save()
    return redirect('customer:fruits')
def addtocartv(request,pid):
    if request.method=='POST':
       product=Addproducts.objects.get(id=pid)
       cart_item,created=Cart.objects.get_or_create(product=product)
       if not created:
           cart_item.quantity+=1
           cart_item.save()
    return redirect('customer:vegetables')
    
def addtocartg(request,pid):
    if request.method=='POST':
       product=Addproducts.objects.get(id=pid)
       cart_item,created=Cart.objects.get_or_create(product=product)
       if not created:
           cart_item.quantity+=1
           cart_item.save()
    return redirect('customer:foodgrains')
def addtocartb(request,pid):
    if request.method=='POST':
       product=Addproducts.objects.get(id=pid)
       cart_item,created=Cart.objects.get_or_create(product=product)
       if not created:
           cart_item.quantity+=1
           cart_item.save()
    return redirect('customer:backery')
   

def remove_from_cart(request,cid):
    if request.method == 'POST':
        cart_item=Cart.objects.get(id=cid)
        cart_item.delete()
    return redirect('customer:viewcart')




def deleteveg(request,pid):
    Addvegetables.objects.get(id=pid).delete()
    
    return redirect('customer:viewcart')