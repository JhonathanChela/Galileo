
from django.urls import path
from . import views
urlpatterns = [
    path('about/', views.about, name="about"),
    path('saludo/<str:usuario>', views.saludo, name="saludo"),
    path('projects/', views.projects, name="projects"),
    path('tasks/', views.tasks, name="tasks"),
    path('create_task/', views.create_task, name="create_task"),
    path('create_project/', views.create_project, name="create_project"),
]