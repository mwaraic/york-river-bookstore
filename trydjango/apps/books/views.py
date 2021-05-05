from django.shortcuts import render
from trydjango.apps.yrb.models import YrbCategory
from trydjango.apps.yrb.dbpostgres import dictfetchall
import psycopg2
# Create your views here.

def category_view(request):
    
  with psycopg2.connect("dbname='YRB' user='postgres' host='127.0.0.1' port='5432' password='maaz'") as connection:
   with connection.cursor() as cursor:
    cursor.execute("SELECT row_number() over (order by cat) as index, initcap(cat) as cat  from yrb_category order by cat;")
   
    all_categories=dictfetchall(cursor)
    context={ 'all_categories' : all_categories
               }
    return render(request, 'category.html', context)