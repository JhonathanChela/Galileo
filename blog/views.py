from django.shortcuts import render
from django.http import HttpResponse, JsonResponse



def index(request):
    template = "index.html"
    print('Estoy en el metodo de invocacion index.html')
    return render(request, template)