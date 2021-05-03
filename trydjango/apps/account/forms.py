from trydjango.apps.yrb.models import YrbCustomer, YrbMember
from django import forms
from django.contrib.auth.models import User
from django.forms import widgets, TextInput, CharField, Widget




class UserForm(forms.ModelForm):
    class Meta:
        model= User    
        fields= ['username', 'password', 'first_name', 'last_name']
        widgets={'username'  : forms.TextInput(attrs={'required': True, 'name': 'username', 'class':'form-control', 'placeholder':'Username', 'type': 'text'}),
                 'first_name': forms.TextInput(attrs={'required': True, 'name': 'first_name', 'class':'form-control', 'placeholder':'First name', 'type': 'text'}),
                 'last_name' : forms.TextInput(attrs={'required': True, 'name': 'last_name', 'class':'form-control', 'placeholder':'Last name', 'type': 'text'}),
                 'password'  : forms.TextInput(attrs={'required': True, 'name': 'password', 'class':'form-control', 'placeholder':'Password', 'type': 'password'})
                 
                 }
    repeatpass= forms.CharField(widget=forms.TextInput(attrs={'required': True, 'name': 'repeatpass', 'class':'form-control', 'placeholder':'Repeat password', 'type': 'password'}))
    city= forms.CharField(widget=forms.TextInput(attrs={'required': True, 'name': 'city', 'class':'form-control', 'placeholder':'City', 'type': 'text'}))
