"""
Сериализаторы DRF для API курсов.
"""
from rest_framework import serializers

from students.models import Course


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор курса: id, name, students."""

    class Meta:
        model = Course
        fields = ("id", "name", "students")
