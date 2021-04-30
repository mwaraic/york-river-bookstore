from django.shortcuts import redirect, render
from passlib.hash import bcrypt, md5_crypt
from .forms import ClubForm, login_auth
# Create your views here.

def club_create_view(request):
    
    form= ClubForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=ClubForm()
    
    
    context={
            'form': form
        }
    return render(request, 'account/account_create.html', context)


def account_login_view(request):
 
  if request.POST or None:
    text1 = request.POST.get('username','')
    text2 = request.POST.get('password','')
    Boolean= login_auth(text1,text2)
    if(Boolean==False):
       return render(request, 'account/account_login.html', {'error':'Incorrect username or password'})
  return render(request, 'account/account_login.html', {})    
    