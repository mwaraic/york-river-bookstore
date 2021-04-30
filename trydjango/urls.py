"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from trydjango.apps.pages.views import club_view, index_view
from trydjango.apps.yrb.views import shop_main
from trydjango.apps.account.views import club_create_view, account_login_view
admin.autodiscover()
urlpatterns = [
    path('club/', club_view, name='club'),
    path('account_create/', club_create_view, name='account_create'),
    path('account_login/', account_login_view, name='account_login'),
    path('index/', index_view, name='index'),
    path('admin/', admin.site.urls)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



