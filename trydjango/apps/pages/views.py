from trydjango.apps.yrb.dbpostgres import dictfetchall
from django.shortcuts import render, redirect
from trydjango.apps.yrb.models import YrbClub, YrbPurchase,YrbCustomer
from trydjango.apps.yrb.dbpostgres import dictfetchall
import psycopg2
from django.contrib.auth.decorators import login_required
from .filters import PurchaseFilter
import datetime
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.




def club_view(request):
 
  all_clubs=YrbClub.objects.all().order_by('club')
  context={ 'all_clubs' : all_clubs}
  
  return render(request,'home.html', context )

def index_view(request):
    
    return render(request, 'index.html', {})
  

@login_required(login_url='account_login') 
def home_view(request):
    
    purchase_filter = PurchaseFilter(request.GET, queryset=YrbPurchase.objects.filter(cid=request.user.id).order_by('-whenp'))
    context={ 'nbar': 'purchase',
              'filter': purchase_filter,
              'year': datetime.datetime.now().year
             }
    
    return render(request, 'purchase.html', context)
@login_required(login_url='account_login')  
def profile_view(request):
  user=User.objects.get(pk=request.user.id)
  Customer=YrbCustomer.objects.get(cid=request.user.id)
  data={'username': user.username, 'first_name': user.first_name, 'last_name': user.last_name, 'city': Customer.city}
  form=UserForm(initial=data)
  context={ 
              'nbar': 'home',
              'form': form}
    
  return render(request, 'profile0.html', context) 
   
@login_required(login_url='account_login')  
def profile_edit_view(request):
  user=User.objects.get(pk=request.user.id)
  Customer=YrbCustomer.objects.get(cid=request.user.id)
  data={'username': user.username, 'first_name': user.first_name, 'last_name': user.last_name, 'city': Customer.city}
  form=UserForm(initial=data)
  if request.method=="POST":
     form=UserForm(request.POST,instance=request.user, initial=data)
     if form.is_valid():
        print('username' in form.changed_data)
        form.save()
        
        name = form.cleaned_data['first_name']+" "+form.cleaned_data['last_name']
        city = form.cleaned_data['city']
        YrbCustomer.objects.filter(cid=request.user.id).update(name=name,city=city) 
        messages.success(request, 'Your profile was updated successfully')    
        return redirect('home')
  
  context={ 
              'nbar': 'home',
              'form': form}
    
  return render(request, 'profile.html', context)  
      
@login_required(login_url='account_login') 
def clubs_view(request):
  with psycopg2.connect("dbname='dbvr7ph65nfv0q' user='epyzanjwjayjxm' host='ec2-18-215-111-67.compute-1.amazonaws.com' port='5432' password='88a7cf9b3959e5cbebcf1ede0aa6c0776741f8488be1ddbe7ba539e7b971bde0'") as connection:
   with connection.cursor() as cursor:
    cursor.execute("SELECT yrb_member.club, count(yrb_purchase.club) from yrb_purchase, yrb_member where yrb_purchase.club= yrb_member.club and yrb_purchase.cid=yrb_member.cid and yrb_purchase.cid= %s group by yrb_member.club order by yrb_member.club;", [request.user.id])
    all_clubs=dictfetchall(cursor)
  
    if all_clubs == []:
       
       cursor.execute("SELECT distinct(yrb_member.club) from yrb_member where yrb_member.cid= %s order by yrb_member.club;", [request.user.id])
       all_clubs=dictfetchall(cursor)
       
       context={ 'all_clubs' : all_clubs,
              'nbar': 'clubs'
               }
    else:
       context={ 'all_clubs' : all_clubs,
              'nbar': 'clubs'
               }
    return render(request, 'clubs.html', context)  