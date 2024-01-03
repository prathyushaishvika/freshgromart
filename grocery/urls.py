
from django.urls import path
from.import views
app_name='groceryadmin'

urlpatterns = [
    
   
     path('additem',views.additem,name='additem'), 
     path('dashboard',views.dashboard,name='dashboard') ,
     path('manageorder',views.manageorder,name='manageorder'),
     path('',views.adminsignup,name='adminsignup'),
     path('adminmaster',views.adminmaster,name='adminmaster'),
     path('adminlogin',views.adminlogin,name='adminlogin'), 
     path('admindashboard',views.admindashboard,name='admindashboard'),
     path('viewproduct',views.viewproduct,name='viewproduct'), 
     path('adminhome',views.adminhome,name='adminhome'),
    

]
