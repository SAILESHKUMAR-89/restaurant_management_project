from django.urls import path
from .views import homepage, about

urlpatterns = [
    path('', homepage, name='home'),
    path('about/', about, name='about'),
    path('contact/', views.contact_view, name='contact'),
]