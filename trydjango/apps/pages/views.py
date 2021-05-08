from django.utils.functional import empty
from trydjango.apps.yrb.dbpostgres import dictfetchall
from django.shortcuts import render
from trydjango.apps.yrb.models import YrbClub, YrbPurchase
from django.db import connection
from trydjango.apps.yrb.dbpostgres import dictfetchall
import psycopg2
from django.contrib.auth.decorators import login_required
from .filters import PurchaseFilter
import datetime
# Create your views here.




def club_view(request):
 
  all_clubs=YrbClub.objects.all().order_by('club')
  context={ 'all_clubs' : all_clubs}
  
  return render(request,'home.html', context )

def index_view(request):
    
    return render(request, 'index.html', {})
  

@login_required(login_url='account_login') 
def home_view(request):
  with psycopg2.connect("dbname='YRB' user='postgres' host='127.0.0.1' port='5432' password='maaz'") as connection:
   with connection.cursor() as cursor:
    cursor.execute("SELECT (ROW_NUMBER () OVER (ORDER BY whenp asc)) as index, club, title, year, whenp, qnty FROM Yrb_purchase WHERE cid = %s order by index desc", [request.user.id])
    
    all_purchases=dictfetchall(cursor)
    purchase_filter = PurchaseFilter(request.GET, queryset=YrbPurchase.objects.filter(cid=request.user.id))
    context={ 'all_purchases' : all_purchases,
              'nbar': 'purchase',
              'filter': purchase_filter,
              'year': datetime.datetime.now().year
             }
    
    return render(request, 'purchase.html', context)
  
@login_required(login_url='account_login')  
def profile_view(request):
  with psycopg2.connect("dbname='YRB' user='postgres' host='127.0.0.1' port='5432' password='maaz'") as connection:
   with connection.cursor() as cursor:
    cursor.execute("SELECT cid, split_part(name,' ', 1) as first_name, split_part(name,' ', 2) as last_name, city FROM Yrb_customer WHERE cid = %s", [request.user.id])
   
    customer=dictfetchall(cursor)
    context={ 'customer' : customer,
              'nbar': 'home' }
    
    return render(request, 'profile.html', context)  
      
@login_required(login_url='account_login') 
def clubs_view(request):
  with psycopg2.connect("dbname='YRB' user='postgres' host='127.0.0.1' port='5432' password='maaz'") as connection:
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