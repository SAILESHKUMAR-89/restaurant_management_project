from django.urls import path
from .views import HardcodedMenuAPIView
from .views import feedback_view, contact_view, menu_view
urlpatterns = [
    path('api/menu/', HardcodedMenuAPIView.as_view(), name = 'menu-api'),
    path('feedback/', feedback_view, name='feedback'),
    path("contact/", contact_view, name="contact"),
    path("menu/", menu_view, name="menu"),
    path("contact/success/", contact_success, name="contact_success"),
]