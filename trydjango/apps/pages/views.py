from trydjango.apps.yrb.dbpostgres import dictfetchall
from django.db.models.aggregates import Count
from django.shortcuts import render
from trydjango.apps.yrb.models import YrbClub, YrbPurchase
from django.forms.models import model_to_dict
from django.db import connection
from trydjango.apps.yrb.dbpostgres import dictfetchall
import psycopg2
from django.contrib.auth.decorators import login_required
# Create your views here.




def club_view(request):
 
  all_clubs=YrbClub.objects.all()
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
    context={ 'all_purchases' : all_purchases,
              'nbar': 'purchase'
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
      
