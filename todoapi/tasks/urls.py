from django.urls import path
from .views import TaskListView,TaskCreateView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),  # Маршрут для получения списка задач
    path('tasks2/', TaskCreateView.as_view(), name='task-list2'),
]
