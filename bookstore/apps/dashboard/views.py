from django.shortcuts import render, redirect
from bookstore.apps.yrb.models import YrbClub, YrbPurchase, YrbCustomer, YrbMember
from django.contrib.auth.decorators import login_required
from .filters import PurchaseFilter
import datetime
from .forms import MemberForm, UserForm
from django.contrib.auth.models import User
from django.contrib import messages


def club_view(request):

    all_clubs = YrbClub.objects.all().order_by('club')
    context = {'all_clubs': all_clubs}

    return render(request, 'home.html', context)


def index_view(request):

    return render(request, 'main.html', {})


@login_required(login_url='account_login')
def home_view(request):

    purchase_filter = PurchaseFilter(request.GET, queryset=YrbPurchase.objects.filter(
        cid=request.user.id).order_by('-whenp'))
    context = {'nbar': 'purchase',
               'filter': purchase_filter,
               'year': datetime.datetime.now().year
               }

    return render(request, 'purchase.html', context)


@login_required(login_url='account_login')
def profile_view(request):
    user = User.objects.get(pk=request.user.id)
    Customer = YrbCustomer.objects.get(cid=request.user.id)
    data = {'username': user.username, 'first_name': user.first_name,
            'last_name': user.last_name, 'city': Customer.city}
    form = UserForm(initial=data)
    context = {
        'nbar': 'home',
                'form': form}

    return render(request, 'profile0.html', context)


@login_required(login_url='account_login')
def profile_edit_view(request):
    user = User.objects.get(pk=request.user.id)
    Customer = YrbCustomer.objects.get(cid=request.user.id)
    data = {'username': user.username, 'first_name': user.first_name,
            'last_name': user.last_name, 'city': Customer.city}
    form = UserForm(initial=data)
    if request.method == "POST":
        form = UserForm(request.POST, instance=request.user, initial=data)
        if form.is_valid():
            form.save()

            name = form.cleaned_data['first_name'] + \
                " "+form.cleaned_data['last_name']
            city = form.cleaned_data['city']
            YrbCustomer.objects.filter(
                cid=request.user.id).update(name=name, city=city)
            messages.success(request, 'Your profile was updated successfully')
            return redirect('home')

    context = {
        'nbar': 'home',
                'form': form}

    return render(request, 'profile.html', context)


@login_required(login_url='account_login')
def clubs_view(request):
    user = User.objects.get(pk=request.user.id)
    form = MemberForm(user, request.POST)
    if request.method == 'POST':
        form = MemberForm(user, request.POST)
        YrbMember.objects.create(cid=YrbCustomer.objects.get(
            cid=request.user.id), club=YrbClub.objects.get(club=form.data['club']))
        messages.success(request, 'Club was added successfully')
        return redirect('clubs')

    context = {'all_clubs': YrbMember.objects.filter(cid=request.user.id),
               'nbar': 'clubs',
               'form': form
               }
    return render(request, 'clubs.html', context)
