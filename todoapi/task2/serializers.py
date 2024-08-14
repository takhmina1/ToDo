from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Task.
    """
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']  # Поля, которые только для чтения

    def validate_title(self, value):
        """
        Проверяет, что название задачи не пустое.
        """
        if not value:
            raise serializers.ValidationError("Название задачи не может быть пустым.")
        return value

    def validate(self, attrs):
        """
        Дополнительная валидация для полей задачи.

    validate(self, attrs):

    Этот метод позволяет выполнить более сложную валидацию,
    которая может затрагивать несколько полей одновременно.
    В этом примере проверяется,
    что если задача помечена как выполненная (completed=True),
    то должно быть указано описание (description).
    Если описание не указано,
    выбрасывается ошибка валидации.

        """
        if 'completed' in attrs and attrs['completed'] and not attrs.get('description'):
            raise serializers.ValidationError("Описание должно быть указано для выполненной задачи.")
        return attrs
