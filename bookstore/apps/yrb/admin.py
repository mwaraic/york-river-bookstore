from django.contrib import admin
from .models import YrbBook, YrbCategory, YrbClub,YrbCustomer, YrbShipping, YrbMember, YrbOffer, YrbPurchase
# Register your models here.

admin.site.register(YrbCategory)
admin.site.register(YrbBook)
admin.site.register(YrbClub)
admin.site.register(YrbCustomer)
admin.site.register(YrbShipping)
admin.site.register(YrbMember)
admin.site.register(YrbOffer)
admin.site.register(YrbPurchase)


