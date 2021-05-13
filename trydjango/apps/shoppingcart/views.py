from django.shortcuts import render
from django.shortcuts import render, redirect
from trydjango.apps.yrb.models import YrbBook, YrbOffer
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# Create your views here.


@login_required(login_url="account_login")
def cart_add(request, offerid):
    cart = Cart(request)
    print(request.POST.get('qnty')) 
    product = YrbOffer.objects.select_related('title__cat').filter(offerid=offerid).first()
    book=YrbBook.objects.filter(title=product.title.title).first()
    cart.add(product=product, quantity=float(request.POST.get('qnty')), weight=float(book.weight))
    return redirect("cart:cart_detail")


@login_required(login_url="account_login")
def item_clear(request, offerid):
    cart = Cart(request)
    product = YrbOffer.objects.get(offerid=offerid)
    cart.remove(product)
    return redirect("cart:cart_detail")


@login_required(login_url="account_login")
def item_increment(request, offerid):
    cart = Cart(request)
    product = YrbOffer.objects.get(offerid=offerid)
    cart.Change(product=product, quantity=float(request.POST.get('qnty')))
    return redirect("cart:cart_detail")


@login_required(login_url="account_login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart:cart_detail")


@login_required(login_url="account_login")
def cart_detail(request):
    
    return render(request, 'cart_detail.html')