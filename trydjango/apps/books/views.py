from trydjango.settings import DATABASES
from typing import BinaryIO

from django.contrib.messages import default_app_config
from trydjango.apps.yrb.models import YrbBook, YrbOffer, YrbClub, YrbCategory, YrbPurchase
from django.shortcuts import render
from trydjango.apps.yrb.dbpostgres import dictfetchall
import os
from .filters import PriceFilter, FilteredListView
import psycopg2
import subprocess
from django.http import Http404

database_url = os.getenv(
    'DATABASE_URL'
)

connection = psycopg2.connect(database_url)
"""
proc = subprocess.Popen('heroku config:get DATABASE_URL -a yorkriverbookstore', stdout=subprocess.PIPE, shell=True)
db_url = proc.stdout.read().decode('utf-8').strip()

connection = psycopg2.connect(db_url)
"""
# Create your views here.

def super_category_view(request):
 
    all_clubs=YrbClub.objects.all()
    context={ 'all_clubs' : all_clubs
               }
    return render(request, 'supercategory.html', context)

  
def category_view(request, club):
   try: 
           club=YrbClub.objects.get(club=club)
   except:
          raise Http404('Page does not exist') 
       
    
   context={ 'all_categories' : YrbCategory.objects.all(),
             'club': club
               }
   return render(request, 'category.html', context)


class BookView(FilteredListView):
  
  filterset_class = PriceFilter
  template_name='booklist.html'  
  paginate_by = 20
  def get_context_data(self,**kwargs):
    context= super().get_context_data(**kwargs)
    try: 
           YrbClub.objects.get(club=self.kwargs.get('club'))
           if(self.kwargs.get('cat').lower()=='all'):
                 pass
           else:
            YrbCategory.objects.get(cat=self.kwargs.get('cat').lower())
    except:
          raise Http404('Page does not exist')
    
    context['all_categories']=YrbCategory.objects.all()
    context['club']=self.kwargs.get('club')
    context['cat']=self.kwargs.get('cat')
    return context

def book_detail_view(request,OfferID):
     try: 
           YrbOffer.objects.get(pk=OfferID)
     except:
          raise Http404('Page does not exist')
     book=YrbOffer.objects.filter(pk=OfferID).values('offerid', 'title', 'price', 'club', 'year', 'title_id__cat', 'title_id__language', 'title_id__weight')
     return render(request, 'book.html', {'book': book})



    
  
