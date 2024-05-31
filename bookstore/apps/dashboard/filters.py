from django.contrib.auth.models import User
from django.forms import widgets
import django_filters
from bookstore.apps.yrb.models import YrbClub, YrbMember, YrbPurchase
from django import forms
import datetime


class PurchaseFilter(django_filters.FilterSet):
    now = datetime.datetime.now()
    title = django_filters.CharFilter(lookup_expr='icontains')
    club = django_filters.ModelChoiceFilter(
        queryset=YrbClub.objects.values_list('club', flat=True))
    whenp = django_filters.NumberFilter(lookup_expr='year')

    class Meta:
        model = YrbPurchase
        fields = ['id', 'cid', 'club', 'title', 'whenp']
