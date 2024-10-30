from app.views import *
from django.urls import path

urlpatterns = [
    path('api/animal/<str:rfid>/', get_animal, name='get_animal'),
]