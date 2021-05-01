from django import forms
from trydjango.apps.yrb.models import YrbClub



class ClubForm(forms.ModelForm):
    class Meta:
        model= YrbClub    
        fields= ['club', 'desp']
        

        
