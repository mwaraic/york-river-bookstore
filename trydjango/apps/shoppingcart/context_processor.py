from .cart import Cart
from trydjango.apps.yrb.models import YrbShipping


def cart_total_amount(request):
 if request.user.is_authenticated:
   cart=Cart(request)
   total_bill = 0.0
   total_weight =0.0
   for key, value in request.session['cart'].items():
	   total_bill=total_bill+(float(value['price'])*value['quantity']) 
    
   for key, value in request.session['cart'].items():
     total_weight= total_weight+ (float(value['weight'])*value['quantity']) 
   list=[[*range(1,500)]]
   a=500
   b=1000
   while b<=YrbShipping.objects.last().weight:
     list.append(range(a,b))
     b+=500
     a+=500
   for ran in list:
    if total_weight in ran:
     shipping=YrbShipping.objects.get(weight=ran[-1]+1).cost
     return {'cart_subtotal_amount' : total_bill, 'cart_total_amount':total_bill+float(shipping), 'cart_shipping': shipping} 
    elif total_weight>YrbShipping.objects.last().weight:
     return {'cart_subtotal_amount' : total_bill,'cart_total_amount':total_bill+float(YrbShipping.objects.last().cost), 'cart_shipping':YrbShipping.objects.last().cost} 
    elif total_weight<=0:
     return {'cart_subtotal_amount' : total_bill,'cart_total_amount':total_bill, 'cart_shipping':0}    
     
 else:
        return {'cart_subtotal_amount' : 0, 'cart_total_amount' : 0,'cart_shipping': 0} 