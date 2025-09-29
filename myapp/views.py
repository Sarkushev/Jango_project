from django.http import HttpResponse

def home(request):
    return HttpResponse("Привет! Это моё первое приложение Django 🚀")
