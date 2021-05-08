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
from django.urls import path, include
from trydjango.apps.pages.views import club_view, index_view, home_view, profile_view, clubs_view
from trydjango.apps.books.views import category_view, super_category_view
from trydjango.apps.account.views import account_create_view, account_login_view, logoutUser
admin.autodiscover()
urlpatterns = [
    path('club/', club_view, name='club'),
    path('account_create/', account_create_view, name='account_create'),
    path('account_login/', account_login_view, name='account_login'), 
    path('logout/', logoutUser, name="logout"),
    path('account/purchase/', home_view, name='purchase'),
    path('account/profile/', profile_view, name='home'),
    path('account/clubs/', clubs_view, name='clubs'),
    path('books/',include('trydjango.apps.books.urls',namespace="books")),
    path('admin/', admin.site.urls)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



