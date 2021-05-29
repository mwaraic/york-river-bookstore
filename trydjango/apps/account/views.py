from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .forms import UserForm
from trydjango.apps.yrb.models import YrbClub, YrbCustomer, YrbMember
from django.contrib.auth.models import User
from django.contrib import messages
import psycopg2
import subprocess
import os
"""
database_url = os.getenv(
    'DATABASE_URL'
)

connection = psycopg2.connect(database_url)
"""
proc = subprocess.Popen('heroku config:get DATABASE_URL -a yorkriverbookstore', stdout=subprocess.PIPE, shell=True)
db_url = proc.stdout.read().decode('utf-8').strip()

connection = psycopg2.connect(db_url)

# Create your views here.

def account_create_view(request):
    if request.user.is_authenticated:
         return redirect('home')
    form=UserForm()
    if request.method=="POST":
     form=UserForm(request.POST)
     if form.is_valid():
        form.save()
        username= form.cleaned_data['username']
        name = form.cleaned_data['first_name']+" "+form.cleaned_data['last_name']
        city = form.cleaned_data['city']
        YrbCustomer.objects.create(cid=User.objects.get(username=username).id, name=name, city=city) 
        YrbMember.objects.create(cid=YrbCustomer.objects.get(cid=User.objects.get(username=username).id), club=YrbClub.objects.get(club='Basic'))
        messages.success(request, 'Your account was created successfully')    
        return redirect('account_login')
    context={
            'form': form
        }
    return render(request, 'account/account_create.html', context)


def account_login_view(request):
  if request.user.is_authenticated:
     return redirect('home')
  if request.method=='POST':
      username=request.POST.get('username')
      password=request.POST.get('password')
      
      user=authenticate(request, username=username, password=password)
      
      if user is not None: 
          login(request, user)
          return redirect('home')
      else:
          messages.error(request,'Username or password not correct')
          return redirect('account_login')
        
    
  context={}
  return render(request, 'account/account_login.html', context)  

def logoutUser(request):
    logout(request)
    return redirect('account_login')
    