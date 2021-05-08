from django import forms
from trydjango.apps.yrb.models import YrbOffer

class BookForm(forms.Form):
    CHOICES= (('1','low to high'),('2','high to low'),)
    select = forms.ChoiceField(widget=forms.Select(attrs={'name': 'select', 'onchange': 'this.form.submit()'}), choices=CHOICES)
    