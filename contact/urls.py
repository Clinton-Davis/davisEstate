from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('sell/', views.sell, name='sell'),
]