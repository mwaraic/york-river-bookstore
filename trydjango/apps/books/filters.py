from django.contrib.auth.models import User
from django.forms import fields, widgets
from django.utils.functional import empty
import django_filters 
from django_filters.filters import NumberFilter
from trydjango.apps.yrb.models import YrbClub, YrbMember, YrbOffer, YrbPurchase
from django import forms
import datetime
from django.views.generic import ListView
from django import forms

class PriceFilter(django_filters.FilterSet):
    
    price= django_filters.OrderingFilter(fields=(
           ('title', 'title'), ('price', 'price'),
        ), empty_label="Featured",
        # labels do not need to retain order
        field_labels={
           'title': 'Sort by name | A to Z', '-title':'Sort by name | Z to A', 'price': 'Sort by price | low to high', '-price':'Sort by price | high to low', 
        })
    
    class Meta:
        modal=YrbOffer
        fields=['title','price']
    def __init__(self, data, *args, **kwargs):
        data = data.copy()
        super().__init__(data, *args, **kwargs)

class FilteredListView(ListView):
    filterset_class = None

    def get_queryset(self):
        # Get the queryset however you usually would.  For example:
        queryset = YrbOffer.objects.select_related('title__cat').filter(title__cat=self.kwargs.get('cat').lower(),club=self.kwargs.get('club'))
        # Then use the query parameters and the queryset to
        # instantiate a filterset and save it as an attribute
        # on the view instance for later.
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        # Return the filtered queryset
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context['filterset'] = self.filterset
        return context
   