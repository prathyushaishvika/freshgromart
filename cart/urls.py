from django.urls import path
from.import views
app_name='addcart'

urlpatterns=[
     path('cart',views.cart,name='cart')
]