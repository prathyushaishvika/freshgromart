
from django.urls import path
from.import views
app_name='customer'

 
urlpatterns =[
    
   path('main',views.main,name='main'),
     path('fruits',views.fruits,name='fruits'),
     path('master',views.master),
     path('vegetables',views.vegetables,name='vegetables'),
     path('foodgrains',views.foodgrains,name='foodgrains'),
     path('backery',views.backery,name='backery'),  
     path('',views.home,name='home'),
     path('logincustomer',views.Login,name='logincustomer'), 
     path('booking',views.booking,name='booking'), 
     path('viewcart',views.viewcart,name='viewcart'),
     path('signup',views.signup,name='signup'), 
     path('payment',views.payment,name='payment'),
     path('changepassword',views.changepassword,name='changepassword'),
     path('category',views.category,name='category') ,
      path('trackorderstatus',views.trackorderstatus,name='trackorderstatus'), 
      path('addtocartf/<int:pid>',views.addtocartf,name='addtocartf'),
      path('addtocartv/<int:pid>',views.addtocartv,name='addtocartv'),
      path('addtocartg/<int:pid>',views.addtocartg,name='addtocartg'),
     path('addtocartb/<int:pid>',views.addtocartb,name='addtocartb'),
     path('remove_from_cart/<int:cid>', views.remove_from_cart, name='remove_from_cart'),
     path('veg_delete/<int:pid>',views.deleteveg,name='veg_delete'),

      

      

      

      

   
 ]
  
  
 