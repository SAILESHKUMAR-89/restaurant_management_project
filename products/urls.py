from django.urls import path
from .views import HardcodedMenuAPIView

urlpatterns = [
    path('api/menu/', HardcodedMenuAPIView.as_view(), name = 'menu-api'),
]