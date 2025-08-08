from django.shortcuts import render
from django.conf import settings

def homepage(request):
    return render(request, 'home/index.html', {
        'restaurant_name': settings.RESTAURANT_NAME
    })
