from django.contrib.auth.models import User
from django.forms import widgets
import django_filters
from trydjango.apps.yrb.models import YrbClub, YrbMember, YrbPurchase
from django import forms



class PurchaseFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    club = django_filters.ModelChoiceFilter(queryset=YrbClub.objects.values_list('club', flat=True))
    whenp= django_filters.NumberFilter(widget=forms.DateInput(attrs={'class': 'form-control', 'id':'datepicker'}), lookup_expr='year')
    
    class Meta:
        model = YrbPurchase
        fields = ['cid','club','title','whenp']
        
    