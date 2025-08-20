from django.urls import path
from .views import HardcodedMenuAPIView
from .views import feedback_view
urlpatterns = [
    path('api/menu/', HardcodedMenuAPIView.as_view(), name = 'menu-api'),
    path('feedback/', feedback_view, name='feedback'),
]