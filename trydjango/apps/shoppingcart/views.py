from django.shortcuts import render
from django.shortcuts import render, redirect
from trydjango.apps.yrb.models import YrbBook, YrbOffer, YrbPurchase
from django.contrib.auth.decorators import login_required
from .cart import Cart
from datetime import datetime 
from django.contrib import messages

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
def review(request):
    
    if len(request.session['cart'].items()) == 0:
       return redirect("cart:cart_detail")
    else: 
       return render(request, 'review.html')


@login_required(login_url="account_login")
def purchase(request):
    if request.method == 'GET':
     
     cart=Cart(request)
     
     value=datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
     
     dt = datetime.strptime(value[:19], '%Y-%m-%d %H:%M:%S')
     
     for key, value in request.session['cart'].items():
      print(value)
      try:
       YrbPurchase.objects.create(cid=value['userid'], qnty=value['quantity'], year=value['year'],club=value['club'], title=value['title'], offerid=YrbOffer.objects.get(offerid=value['product_id']),whenp=dt) 
      except:
        messages.error(request, 'You are not the member of club offering the book. Kindly register.') 
        return redirect("clubs") 
     messages.success(request, 'Thank you for purchasing @ York River Bookstore')
     Cart.clear(cart) 
     return redirect("books:super") 
       

@login_required(login_url="account_login")
def item_increment(request, offerid):
    cart = Cart(request)
    product = YrbOffer.objects.get(offerid=offerid)
    print(request.POST.get('qnty'))
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