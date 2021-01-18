from django.contrib import admin
from django.urls import path, include
from . import views 


urlpatterns = [
path('profile/', views.profile, name='profile'),
path('order-form/',views.createOrder, name='order-form'),
path('update_order/<str:pk>/',views.updateOrder, name='update_order'), # passing in the primary key of the request objet into the url
path('delete_item/<str:pk>/',views.delete_item, name='delete_order'),
path('add_client', views.addClient, name='add_client'),
path('edit_client/<str:pk>/', views.editClient, name='edit_client')
]