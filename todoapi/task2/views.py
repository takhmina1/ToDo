from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializers import TaskSerializer
from .services import (
    create_task, 
    update_task, 
    delete_task, 
    get_filtered_tasks, 
    get_task_by_id
)

class TaskViewSet(viewsets.ViewSet):
    """
    ViewSet для управления задачами.
    """

    def list(self, request):
        """
        Возвращает список задач. Можно фильтровать по статусу выполнения.
        """
        completed = request.query_params.get('completed')
        tasks = get_filtered_tasks(completed=completed)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Возвращает конкретную задачу по её идентификатору.
        """
        task = get_task_by_id(pk)
        if task is not None:
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        return Response({'detail': 'Задача не найдена.'}, status=status.HTTP_404_NOT_FOUND)

    # def create(self, request):
    #     """
    #     Создает новую задачу.
    #     """
    #     task = create_task(request.data)
    #     serializer = TaskSerializer(task)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """
        Обновляет существующую задачу.
        """
        task = update_task(pk, request.data)
        if task is not None:
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        return Response({'detail': 'Задача не найдена.'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        """
        Удаляет задачу.
        """
        success = delete_task(pk)
        if success:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'detail': 'Задача не найдена.'}, status=status.HTTP_404_NOT_FOUND)
