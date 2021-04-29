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
from trydjango.apps.pages.views import home_view, index_view
from trydjango.apps.yrb.views import shop_main
admin.autodiscover()
urlpatterns = [
    path('', home_view, name='home'),
    path('shop/', shop_main, name='shop'),
    path('index/', index_view, name='index'),
    path('admin/', admin.site.urls)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



