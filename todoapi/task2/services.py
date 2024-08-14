from .models import Task

def create_task(data):
    """
    Создание новой задачи с заданными данными.
    """
    task = Task.objects.create(
        title=data.get('title'),
        description=data.get('description', ''),
        completed=data.get('completed', False)
    )
    return task

def update_task(task_id, data):
    """
    Обновление существующей задачи по идентификатору.
    """
    try:
        task = Task.objects.get(id=task_id)
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.completed = data.get('completed', task.completed)
        task.save()
        return task
    except Task.DoesNotExist:
        return None

def delete_task(task_id):
    """
    Удаление задачи по идентификатору.
    """
    try:
        task = Task.objects.get(id=task_id)
        task.delete()
        return True
    except Task.DoesNotExist:
        return False

def get_filtered_tasks(completed=None):
    """
    Получение списка задач с возможностью фильтрации по статусу выполнения.
    """
    if completed is not None:
        return Task.objects.filter(completed=completed.lower() == 'true')
    return Task.objects.all()

def get_task_by_id(task_id):
    """
    Получение задачи по идентификатору.
    """
    try:
        return Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return None
    except  Exception as e:
        print(f'{e}')
    # else:
    #     res
    # return res