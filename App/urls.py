from django.urls import path,include
from .views import *

urlpatterns = [
    path('products',productapi.as_view())
]