from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.index, name='index'),
    path('admin-login', views.admin_login, name='admin_login'),
    path('store/', views.store, name='store'),
    path('home/', views.home_page, name='home-page'),
    path('cart/', views.cart, name='cart'),
    path('update_item/', views.updateItem, name='update-item'),
    path('process_order/', views.processOrder, name='process-order'),
    path('checkout/', views.checkout, name='checkout'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.register, name='register'),
    path('profile', views.user_dashboard, name='user-dashboard'),
    path('chart/', views.chart, name='chart'),
    path('table/', views.table, name='table'),
    path('password/', views.password, name='password'),
    path('akom-admin', views.admin_dashboard, name='admin-dashboard'),
]
