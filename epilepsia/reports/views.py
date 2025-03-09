from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.core.cache import cache
import time

def generate_report(request):
    """
    Simula la generación de un reporte clínico.
    Se usa caché para evitar procesar repetidamente el mismo reporte.
    """
    report_key = 'clinical_report'
    cached_report = cache.get(report_key)

    if cached_report:
        # Se devuelve el reporte si ya está en caché.
        return JsonResponse({'report': cached_report, 'cached': True})

    # Simulacion del reporte
    time.sleep(2)  

    # Datos de ejemplo para el reporte
    report_data = {
        'patient': 'John Doe',
        'diagnosis': 'Epilepsia',
        'date': '2025-03-09',
        'details': 'Detalle del reporte clínico...'
    }

    # Se almacena en caché por 5 minutos (300 segundos)
    cache.set(report_key, report_data, 300)

    return JsonResponse({'report': report_data, 'cached': False})
