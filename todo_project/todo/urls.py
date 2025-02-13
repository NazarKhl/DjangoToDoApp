from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  
    path('update_status/<int:task_id>/', views.update_task_status, name='update_task_status'),
]
