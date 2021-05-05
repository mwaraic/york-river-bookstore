from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .forms import UserForm
from trydjango.apps.yrb.models import YrbClub, YrbMember, YrbCustomer
from django.contrib.auth.models import User
import psycopg2
from django.contrib import messages

from django.core.exceptions import ValidationError
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
        with psycopg2.connect("dbname='YRB' user='postgres' host='127.0.0.1' port='5432' password='maaz'") as connection:
          with connection.cursor() as cursor:
           cursor.execute("INSERT INTO yrb_member(cid, club) select id, 'Basic' from auth_user where id=%s;", [User.objects.get(username=username).id])
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
    