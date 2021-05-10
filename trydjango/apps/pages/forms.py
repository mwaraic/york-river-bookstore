from trydjango.apps.yrb.models import YrbCustomer, YrbMember
from django import forms
from django.contrib.auth.models import User
from django.forms import widgets, TextInput, CharField, Widget
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from trydjango.settings import AUTH_PASSWORD_VALIDATORS

class UserForm(forms.ModelForm):
    class Meta:
        model= User    
        fields= ['username','first_name', 'last_name']
        widgets={'username'  : forms.TextInput(attrs={'name': 'username', 'class':'form-control',  'type': 'text'}),
                 'first_name': forms.TextInput(attrs={'name': 'first_name', 'class':'form-control', 'type': 'text'}),
                 'last_name' : forms.TextInput(attrs={'name': 'last_name', 'class':'form-control','type': 'text'}),
                 }
    city= forms.CharField(widget=forms.TextInput(attrs={'name': 'city', 'class':'form-control', 'type': 'text'}))
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(UserForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['username'].required = False
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['city'].required = False
        
    def clean_username(self):
       if self.cleaned_data['username'].strip() == '':
            raise ValidationError('This field cannot be blank!')
       return self.cleaned_data['username']
    def clean_first_name(self):
       if self.cleaned_data['first_name'].strip() == '':
            raise ValidationError('This field cannot be blank!')
       return self.cleaned_data['first_name']
    def clean_last_name(self):
       if self.cleaned_data['last_name'].strip() == '':
            raise ValidationError('This field cannot be blank!')
       return self.cleaned_data['last_name']
    def clean_city(self):
       if self.cleaned_data['city'].strip() == '':
            raise ValidationError('This field cannot be blank!')
       return self.cleaned_data['city']
   
   
        