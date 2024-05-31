from django.shortcuts import render
from django.shortcuts import render, redirect
from bookstore.apps.yrb.models import YrbBook, YrbOffer, YrbPurchase, YrbMember
from django.contrib.auth.decorators import login_required
from .cart import Cart
from datetime import datetime
from django.contrib import messages


@login_required(login_url="account_login")
def cart_add(request, offerid):
    cart = Cart(request)
    product = YrbOffer.objects.select_related(
        'title__cat').filter(offerid=offerid).first()
    book = YrbBook.objects.filter(title=product.title.title).first()
    cart.add(product=product, quantity=float(
        request.POST.get('qnty')), weight=float(book.weight))
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
        cart = Cart(request)
        value = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        dt = datetime.strptime(value[:19], '%Y-%m-%d %H:%M:%S')

        for key, item in request.session['cart'].items():
            offer_id = item.get('product_id')
            club_id = item.get('club')
            # Check if the user is a member of the club offering the book
            if not YrbMember.objects.filter(cid=request.user.id, club=club_id).exists():
                messages.error(request, 'You are not a member of the club offering the book. Kindly register.')
                return redirect("clubs")  # Redirect to club registration page
            try:
                YrbPurchase.objects.create(
                    cid=item['userid'],
                    qnty=item['quantity'],
                    year=item['year'],
                    club=item['club'],
                    title=item['title'],
                    offerid=YrbOffer.objects.get(offerid=offer_id),
                    whenp=dt
                )
            except:
                messages.error(request, 'Error occurred while processing the purchase.')
                return redirect("books:super")  # Redirect to books page or any other appropriate page

        messages.success(request, 'Thank you for purchasing at York River Bookstore')
        Cart.clear(cart)
        return redirect("books:super")  # Redirect to books page or any other appropriate page


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
