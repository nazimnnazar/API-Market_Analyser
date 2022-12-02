from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.Frontpage,name='Frontpage'),
    path('register',views.Register,name='register'),
    path('login',views.loginpage,name='login'),
    path('logout',views.logoutuser,name='logout'),
    # path('chart',views.chart,name='chart'),
]
