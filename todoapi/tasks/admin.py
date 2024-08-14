from django.contrib import admin
from .models import Task  # Импортируем модель Task

class TaskAdmin(admin.ModelAdmin):
    """
    Настройки административного интерфейса для модели Task.
    """
    list_display = ('id', 'title', 'completed', 'created_at')  # Поля, отображаемые в списке задач
    search_fields = ('title',)  # Поля, по которым можно выполнять поиск
    list_filter = ('completed',)  # Фильтр по статусу выполнения задач
    ordering = ('-created_at',)  # Сортировка по дате создания (последние сначала)

# Регистрация модели Task в админке с использованием класса TaskAdmin
admin.site.register(Task, TaskAdmin)
