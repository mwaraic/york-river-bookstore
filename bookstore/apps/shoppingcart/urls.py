from django.urls import path
from .import views
from .import apps

app_name = apps.ShoppingcartConfig.name

urlpatterns = [
    path('add/<int:offerid>', views.cart_add, name='cart_add'),
    path('item_clear/<int:offerid>/', views.item_clear, name='item_clear'),
    path('item_increment/<int:offerid>/',
         views.item_increment, name='item_increment'),
    path('cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart-detail/', views.cart_detail, name='cart_detail'),
    path('review/', views.review, name='review'),
    path('purchase/', views.purchase, name='purchase')
]
