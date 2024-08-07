
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from.models import Project, Task
from.forms import CreateNewTask, CreateNewProject

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
    template='project/project.html'
    return render(request, template,{
        'projects':projects
    })

def tasks(request):
    template='task/task.html'
    tasks = Task.objects.all()
    return render(request, template,{
        'tasks':tasks
    })

def create_task(request):
    if request.method == 'POST':
        Task.objects.create(title=request.POST['title'],
                            description=request.POST['description'],
                            project_id=1)
        return redirect('/home/tasks/')
    else:
        return render(request, 'task/create_task.html',
                  {
                      'form':CreateNewTask()
                  })

def create_project(request):
    if request.method == 'POST':
        Project.objects.create(name=request.POST['name'])
        return redirect('/home/projects/')
    else:
        return render(request, 'project/create_project.html',
                  {
                      'form':CreateNewProject()
                  })