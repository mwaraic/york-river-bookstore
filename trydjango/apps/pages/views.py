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
    cursor.execute("SELECT * FROM Yrb_purchase WHERE cid = %s order by whenp desc", [request.user.id])
   
    all_purchases=dictfetchall(cursor)
    context={ 'all_purchases' : all_purchases}
    
    return render(request, 'profile.html', context)
