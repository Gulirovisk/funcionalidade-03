from app.models import *
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os

# # Create your views here.
# def get_animal(request, rfid):
#     try:
#         animal = Animal.objects.get(rfid=rfid)

#         data = {'id': animal.id, 'identificacao_unica': animal.identificacao_unica, 'rfid': animal.rfid}

#         print(data)

#         # return JsonResponse(data, status=200)
#         return JsonResponse(data, status=200)
#     except Animal.DoesNotExist:
#         return JsonResponse({'error': 'Animal not found'}, status=404)
    
# def animal_page(request):
#     return render(request, 'animal.html')

# Armazenar o animal mais recente lido em memória (ou em um cache)
latest_animal_data = None

@csrf_exempt
def get_animal(request, rfid):
    global latest_animal_data

    try:
        animal = Animal.objects.get(rfid=rfid)
        data = {
            'id': animal.id,
            'identificacao_unica': animal.identificacao_unica,
            'nome': animal.nome,
            'rfid': animal.rfid,
            'foto': animal.foto.url if animal.foto else os.path.join(settings.MEDIA_URL, 'bois/guliro.jpg'),
        }

        latest_animal_data = data  # Armazena os dados lidos

        return JsonResponse(data, status=200)
    except Animal.DoesNotExist:
        return JsonResponse({'error': 'Animal not found'}, status=404)

def latest_animal(request):
    """Retorna os dados do animal mais recente lido."""
    if latest_animal_data:
        return JsonResponse(latest_animal_data, status=200)
    else:
        return JsonResponse({'error': 'No data available'}, status=404)
    
def index(request):
    return render(request, 'index.html')