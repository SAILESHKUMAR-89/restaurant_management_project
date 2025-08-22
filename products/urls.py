from django.urls import path
from .views import HardcodedMenuAPIView
from .views import feedback_view, contact_view
urlpatterns = [
    path('api/menu/', HardcodedMenuAPIView.as_view(), name = 'menu-api'),
    path('feedback/', feedback_view, name='feedback'),
    path("contact/", contact_view, name="contact"),
]