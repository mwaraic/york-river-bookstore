from django.shortcuts import render

# Create your views here.

def shop_main(request):
    
    return render(request, 'home.html', {})