from app.views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    # path('animal/', animal_page, name='animal_page'),  # URL para a página HTML
    path('api/animal/<str:rfid>/', get_animal, name='get_animal'),
    path('api/latest-animal/', latest_animal, name='latest_animal'),
]