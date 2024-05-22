from django.urls import path, include
from tasks import views

urlpatterns = [
    path('', views.tasks_list, name='tasks_list'),
    path('completed', views.tasks_completed, name='tasks_completed'),
    path('add/', views.add_task, name='add_task'),
]
