
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from.models import Project, Task

# Create your views here.
def saludo(request, usuario):
    #print(usuario)
    return HttpResponse("Hola: "+ usuario)

def about(request):
    return HttpResponse("About!")

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request):
    return HttpResponse("tasks")