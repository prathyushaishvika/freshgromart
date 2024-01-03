
from django.urls import path
from.import views



app_name='productadmin'
urlpatterns=[

     path('',views.addproduct,name='addproduct'), 
     path('viewproduct',views.viewproduct,name='viewproduct'),
     path('productmaster',views.productmaster,name='productmaster'),
     path('p_delete/<int:pid>',views.deleteproduct,name='p_delete'),
     path('p_update/<int:pid>',views.updateproduct,name='p_update'),
     path('statusupdate/<int:pid>',views.statusupdate,name='status_update')
]
