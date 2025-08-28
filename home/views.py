from django.shortcuts import render
from django.conf import settings

def homepage(request):
    cart = request.session.get("cart", [])
    cart_count = len(cart)

    context = {
        "restaurant_name":"My Restaurant",
        "restaurant_phone":"123-456-7890",
        "cart_count":cart_count,
    }
    return render(request, 'home/index.html', {
        'restaurant_name': settings.RESTAURANT_NAME,
        'restaurant_phone': settings.restaurant_phone
    })
def contact_view(request):
    return render(request, "contact.html", {"restaurant_name": "Sailesh's Bistro"})