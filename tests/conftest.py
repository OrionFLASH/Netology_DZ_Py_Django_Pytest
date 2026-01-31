"""
Общие фикстуры pytest для тестов API.

Фикстуры:
- api_client: клиент DRF для запросов к API;
- course_factory: фабрика курсов (model_bakery);
- student_factory: фабрика студентов (model_bakery).
"""
import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from students.models import Course, Student


@pytest.fixture
def api_client() -> APIClient:
    """Клиент для выполнения запросов к API (DRF APIClient)."""
    return APIClient()


@pytest.fixture
def course_factory():
    """
    Фабрика курсов на основе model_bakery.baker.

    Использование: course = course_factory(name="Python")
    или course_factory(_quantity=3) для нескольких курсов.
    """
    def _factory(**kwargs) -> Course | list[Course]:
        return baker.make(Course, **kwargs)
    return _factory


@pytest.fixture
def student_factory():
    """
    Фабрика студентов на основе model_bakery.baker.

    Использование: student = student_factory(name="Иван")
    или student_factory(_quantity=5) для нескольких студентов.
    """
    def _factory(**kwargs) -> Student | list[Student]:
        return baker.make(Student, **kwargs)
    return _factory
