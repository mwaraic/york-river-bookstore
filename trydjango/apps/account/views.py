from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .forms import UserForm
from trydjango.apps.yrb.models import YrbClub

# Create your views here.

def account_create_view(request):
    all_clubs= YrbClub.objects.all()
    form= UserForm(request.POST or None)
    if form.is_valid():
        form.save()
    context={
            'form': form,
            'all_clubs': all_clubs
        }
    return render(request, 'account/account_create.html', context)


def account_login_view(request):
  if request.user.is_authenticated:
     return redirect('home')
  if request.method=='POST':
      username=request.POST.get('username')
      password=request.POST.get('password')
      
      user=authenticate(request, username=username, password=password)
      
      if user is not None: 
          login(request, user)
          return redirect('home')
        
    
  context={}
  return render(request, 'account/account_login.html', context)  

def logoutUser(request):
    logout(request)
    return redirect('account_login')
    