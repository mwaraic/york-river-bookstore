from django.urls import path, include
from .import views
from .import apps
from .views import BookView
app_name= apps.BooksConfig.name

urlpatterns = [
    path('', views.super_category_view, name="super"),
    path('<str:club>/', views.category_view, name="category"),
    path('<str:club>/<str:cat>',BookView.as_view(), name="booklist"),
]
