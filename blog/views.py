from django.shortcuts import render
from django.http import HttpResponse, JsonResponse



def index(request):
    texto='Bienvenido'
    template = "index.html"
    return render(request, template,{
        'texto': texto
    })