
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from.models import Project, Task

# Create your views here.
def saludo(request, usuario):
    #print(usuario)
    return HttpResponse("Hola: "+ usuario)

def about(request):
    template = 'about.html'
    return render(request, template)
    #return HttpResponse("About!")

def projects(request):
    #projects = list(Project.objects.values())
    #return JsonResponse(projects, safe=False)
    projects = Project.objects.all()
    template='project.html'
    return render(request, template,{
        'projects':projects
    })

def tasks(request):
    template='task.html'
    return render(request, template)
    #return HttpResponse("tasks")