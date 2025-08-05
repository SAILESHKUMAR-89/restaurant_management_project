from django.urls import path
from .views import HardcodedMenuAPIView

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('menu/', HardcodedMenuAPIView.as_view(), name = 'hardcoded-menu'),
]