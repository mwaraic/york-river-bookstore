from django.contrib.auth.models import User
import django_filters
from trydjango.apps.yrb.models import YrbClub, YrbMember, YrbPurchase

class PurchaseFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    club = django_filters.ModelChoiceFilter(queryset=YrbClub.objects.values_list('club', flat=True))
    whenp = django_filters.NumberFilter(field_name='whenp', lookup_expr='year')
    whenp__gt = django_filters.NumberFilter(field_name='whenp', lookup_expr='year__gte')
    whenp__lt = django_filters.NumberFilter(field_name='whenp', lookup_expr='year__lt')
    class Meta:
        model = YrbPurchase
        fields = ['cid','club','title','whenp']
    