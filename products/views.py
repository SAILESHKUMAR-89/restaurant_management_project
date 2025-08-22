from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

# Create your views here.
class HardcodedMenuAPIView(APIView):
    def get(self, request):
        try:
            data = [
                {
                    "name": "Margherita Pizza",
                    "description": "Classic cheese pizza with tomato sauce",
                    "price": 250
                },
                {
                    "name": "Veg Burger",
                    "description": "Crispy patty with lettuce and mayo",
                    "price": 120
                },
                {
                    "name": "Paste alfredo",
                    "description": "White sauce pasta with vegetables",
                    "price": 200
                }
            ]
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            #catch my unexpected errors
            return Response(
                {"error": "Something went wrong while fetching the menu.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == "POST";
        from = FeedbackForm(request, POST)
        if form.is_valid();
            form.save()
            return redirect('feedback')
        else:
            form = FeedbackForm()
        return render(request, 'feedback.html', {'form': form})

from .models import RestaurantLocation

def homepage(request):
    location = RestaurantLocation.objects.first()
    context = {
        "restaurant_name": "My Restaurant",
        "restaurant_phone": "+91-9876543210",
        "location":location,
    }
    return render(request, "index.html", context)