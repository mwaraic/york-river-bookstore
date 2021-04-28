from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):   
 render(request,'base.html',{})