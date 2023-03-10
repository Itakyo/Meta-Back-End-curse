###pagina nueva implementada para la administracion de errores########
from django.http import  HttpResponse, HttpResponseNotFound

def handler404(request, exception):
    return HttpResponse("404: Page not found!! <br><br> <button onclick="" href='';""> Go to Homepage</button>")

def home(request):
    return HttpResponseNotFound("Little Lemon!")