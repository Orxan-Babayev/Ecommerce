from django.urls import path
from core.views import home, contact, error

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('404/', error, name='404'),
]
