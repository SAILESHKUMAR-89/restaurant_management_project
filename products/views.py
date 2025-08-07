from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

# Create your views here.
class HardcodedMenuAPIView(APIView):
    deg get(self, request):
    data = [
        {
            "name": "Margherita Pizza",
            "description": "Classic cheese pizza with tomato sauce",
            "price": 250
        },
        {
            "name": "Veg Burger",
            "desciption": "Crispy patty with lettuce and mayo",
            "price": 120
        },
        {
            "name": "Paste alfredo",
            "description": "White sauce pasta with vegetables",
            "price": 200
        }
    ]
    return Response(data, status=status.HTTP_200_OK)

    

