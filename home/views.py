from django.shortcuts import render
from django.conf import settings

def homepage(request):
    return render(request, 'home/index.html', {
        'restaurant_name': settings.RESTAURANT_NAME
    })
def contact_view(request):
    return render(request, "contact.html", {"restaurant_name": "Sailesh's Bistro"})