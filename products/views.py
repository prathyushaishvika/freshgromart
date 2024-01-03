from django.shortcuts import render,redirect
from.models import *
from django.http import JsonResponse


# Create your views here.

def productmaster(request):
    return render(request,'products/productmaster.html')




def addproduct(request):
        if request.method=='POST':
           name=request.POST['name']
           price=request.POST['price']
           
           image = request.FILES.get('images')
           
           
           status=request.POST['status'] 

           items=Addproducts(name=name,price=price,img=image,status=status)
           items.save()
           
           return redirect('productadmin:viewproduct')  
           
        return render(request,'products/addproduct.html')   


def viewproduct(request):
    pdts=Addproducts.objects.all()
    veg=Addvegetables.objects.all()
    baks=Addbackery.objects.all()
    fdgs=Addfoodgrain.objects.all()
    return render (request,'products/viewproduct.html',{'product':pdts,
                                                        'vegetable':veg,
                                                        'backery':baks,
                                                        'foodgrain':fdgs
                                                        })

def deleteproduct(request,pid):
     Addproducts.objects.get(id=pid).delete()
    
     return redirect('productadmin:viewproduct')


def updateproduct(request,pid):
     pdt=Addproducts.objects.get(id=pid)
    
     if request.method=='POST':
          name=request.POST['name']
          price=request.POST['price']
          image=request.FILES.get('images')
          
          pdt.name=name
          pdt.price=price
          pdt.image=image
         

          pdt.save()
          return redirect('productadmin:viewproduct')
     return render(request,'products/updateproduct.html',{'product':pdt,
                                                       
                                                          })

def statusupdate(request,pid):
     p_status=Addproducts.objects.get(id=pid)
     p_veg=Addvegetables.objects.get(id=pid)
     p_backery=Addbackery.objects.get(id=pid)
     p_foodgrain=Addfoodgrain.objects.get(id=pid)

     if p_status.status=='0':
          Addproducts.objects.filter(id=pid).update(status='1')

     else:
          Addproducts.objects.filter(id=pid).update(status='0')


     if p_veg.status=='0':
          Addvegetables.objects.filter(id=pid).update(status='1')

     else:
          Addvegetables.objects.filter(id=pid).update(status='0')


     if p_backery.status=='0':
          Addbackery.objects.filter(id=pid).update(status='1')
     else:
          Addbackery.objects.filter(id=pid).update(status='0')
          

     if p_foodgrain.status=='0':
          Addfoodgrain.objects.filter(id=pid).update(status='1')
     else:
          Addfoodgrain.objects.filter(id=pid).update(status='0')

     return redirect('productadmin:viewproduct')

        
def addvegetable(request):
      if request.method=='POST':
           name=request.POST['name']
           price=request.POST['price']
           
           image = request.FILES.get('images')
           
           status=request.POST['status'] 

           items=Addvegetables(name=name,price=price,img=image,status=status)
           items.save()
           
           return redirect('productadmin:viewproduct')  
           
      return render(request,'products/addproduct.html')   


def addbackery(request):
      if request.method=='POST':
           name=request.POST['name']
           price=request.POST['price']
           
           image = request.FILES.get('images')
           status=request.POST['status'] 

           items=Addbackery(name=name,price=price,img=image,status=status)
           items.save()
           
           return redirect('productadmin:viewproduct')  
           
      return render(request,'products/addproduct.html')  
 
def addfoodgrain(request):
     if request.method=='POST':
          name=request.POST['name']
          price=request.POST['price']
          image=request.FILES.get('images')
          status=request.POST['status']
          items=Addfoodgrain(name=name,price=price,img=image,status=status)
          items.save()
           
          return redirect('productadmin:viewproduct')  
           
     return render(request,'products/addproduct.html')  

          