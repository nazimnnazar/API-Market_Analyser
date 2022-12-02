from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
import requests
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout

def Frontpage(request):
   apidata = requests.get(
      'https://api.coingecko.com/api/v3/coins/markets?vs_currency=inr&order=market_cap_desc&per_page=100&page=1&sparkline=false'
      ).json()
   return render(request,'FrontPage.html',{'apidata':apidata})

def Register(request):
   form=CreateUserForm()

   if request.method == 'POST':
      form=CreateUserForm(request.POST)
      if form.is_valid():
         form.save()
         user = form.cleaned_data.get('username')
         messages.success(request,'account was created for' + user)
         return redirect('login')
   context={'form':form}
   return render(request,'register.html',context)

def loginpage(request):
   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(request,username=username,password=password)
      if user is not None:
         login(request,user)
         return redirect('/')
      else:
         messages.info(request,'Username OR password is incorrect')
         return render(request,'login.html')
   context={}
   return render(request,'login.html',context)

def logoutuser(request):
   logout(request)
   return redirect('login')

# def chart(request):
#    return render(request,'chart.html')