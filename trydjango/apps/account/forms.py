from django import forms
from trydjango.apps.yrb.models import YrbUser, YrbClub
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from passlib.hash import md5_crypt

class ClubForm(forms.ModelForm):
    class Meta:
        model= YrbClub    
        fields= ['club', 'desp']
        
def login_auth(username, password):
    users = YrbUser.objects.all();
    for user in users:
        if(user.email==username):
          if(md5_crypt.verify(password, user.password_hash)):
            return True
          
   
    return False
        
