from app.models import *
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def get_animal(request, rfid):
    try:
        animal = Animal.objects.get(rfid=rfid)

        data = {
            'identificacao_unica': animal.identificacao_unica,
            'rfid': animal.rfid,
        }

        return JsonResponse(data, status=200)
    except Animal.DoesNotExist:
        return JsonResponse({'error': 'Animal not found'}, status=404)