from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    """
    Админский интерфейс для модели Task.
    """
    list_display = ('title', 'completed', 'created_at', 'updated_at')  # Показать указанные поля
    list_filter = ('completed',)  # Фильтрация по выполненным задачам
    search_fields = ('title', 'description')  # Поиск по заголовку и описанию
    ordering = ('-created_at',)  # Сортировка по дате создания
    date_hierarchy = ('created_at')  # Навигация по датам
    # Если у вас есть поле slug, раскомментируйте следующую строку
    # prepopulated_fields = {'slug': ('title',)}

admin.site.register(Task, TaskAdmin)
