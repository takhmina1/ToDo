from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

class TaskListView(generics.ListAPIView):
    """
    Представление для получения списка задач.
    """
    queryset = Task.objects.all()  # Получаем все задачи из базы данных
    serializer_class = TaskSerializer  # Указываем сериализатор для использования

    def get(self, request, *args, **kwargs):
        """
        Обрабатываем GET-запрос и возвращаем список задач.
        """
        tasks = self.get_queryset()  # Получаем список задач
        serializer = self.get_serializer(tasks, many=True)  # Сериализуем данные
        return Response(serializer.data, status=status.HTTP_200_OK)  # Возвращаем данные с статусом 200




class TaskCreateView(generics.CreateAPIView):
    """
    Представление для создания новой задачи.
    """
    queryset = Task.objects.all()  # Получаем все задачи из базы данных
    serializer_class = TaskSerializer  # Указываем сериализатор для использования

    def post(self, request, *args, **kwargs):
        """
        Обрабатываем POST-запрос и создаем новую задачу.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()  # Сохраняем новую задачу в базе данных


        