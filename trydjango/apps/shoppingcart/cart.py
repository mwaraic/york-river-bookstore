
from decimal import Decimal
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect


class Cart(object):

    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity, weight,action=None):
        """
        Add a product to the cart or update its quantity.
        """
        id = product.offerid
        newItem = True
        if str(product.offerid) not in self.cart.keys():

            self.cart[product.offerid] = {
                'userid': self.request.user.id,
                'product_id': product.offerid,
                'title': product.title.title,
                'quantity': quantity,
                'price': str(product.price),
                'weight': weight,
                'club': product.club.club,
                'year': product.year
                
            }
        else:
            newItem = True

            for key, value in self.cart.items():
                if key == str(product.offerid):

                    value['quantity'] = value['quantity'] + quantity
                    newItem = False
                    self.save()
                    break
            if newItem == True:

                self.cart[product.offerid] = {
                    'userid': self.request,
                    'product_id': product.offerid,
                    'title': product.title.title,
                    'quantity': quantity,
                    'price': str(product.price),
                    'weight': weight,
                    'club': product.club.club,
                    'year': product.year
                }

        self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.offerid)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def Change(self,product, quantity):
        for key, value in self.cart.items():
            if key == str(product.offerid):
               print(quantity)
               value['quantity'] = quantity
               self.save()
               break
            else:
                print("Something Wrong")

    def clear(self):
        # empty cart
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True