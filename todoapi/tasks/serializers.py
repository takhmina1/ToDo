from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'  # Выбор всех полей модели Task

    def validate_title(self, value):
        # Валидация заголовка задачи
        if len(value) < 5:
            raise serializers.ValidationError("Заголовок задачи должен содержать не менее 5 символов.")
        return value

    def validate(self, data):
        # Валидация, чтобы не отмечать задачу как выполненную без описания
        if data.get('completed') and not data.get('description'):
            raise serializers.ValidationError("Невозможно отметить задачу как выполненную без описания.")
        return data
