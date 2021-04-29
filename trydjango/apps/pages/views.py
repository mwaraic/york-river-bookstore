from django.db.models.aggregates import Count
from django.shortcuts import render
from trydjango.apps.yrb.models import YrbClub
from django.forms.models import model_to_dict
# Create your views here.






def home_view(request):
 
  
  all_clubs=YrbClub.objects.all()
  
  context={ 'all_clubs' : all_clubs}

 
  return render(request,'home.html', context )

def index_view(request):
    
    return render(request, 'index.html', {})
 
