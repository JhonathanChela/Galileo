
from django.urls import path
from . import views
urlpatterns = [
    path('about/', views.about),
    path('saludo/<str:usuario>', views.saludo),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
]