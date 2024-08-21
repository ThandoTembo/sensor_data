from django.shortcuts import render
from django.http import JsonResponse
from .models import SensorData

def receive_data(request):
    if request.method == 'POST':
        temperature = request.POST.get('temperature')
        humidity = request.POST.get('humidity')
        if temperature and humidity:
            SensorData.objects.create(temperature=temperature, humidity=humidity)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid data'})
    return JsonResponse({'status': 'error', 'message': 'Only POST requests allowed'})

def display_data(request):
    data = SensorData.objects.order_by('-timestamp')[:10]
    return render(request, 'sensor_data/index.html', {'data': data})
