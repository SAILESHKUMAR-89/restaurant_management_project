from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm

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
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
             return render(request, "contact_success.html", {'name':name})
    else:
        form = ContactForm()
    return render(request, "contact.html", {"restaurant_name": "Sailesh's Bistro"})

def homepage(request):
    return render(request, "homepage.html", {
        "restaurant_phone": settings.RESTAURANT_PHONE
    })

def privacy_view(request):
    return render(request, "privacy.html")