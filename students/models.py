"""
Модели приложения students: студенты и курсы.
"""
from django.db import models


class Student(models.Model):
    """Студент: имя и дата рождения."""

    name = models.TextField()
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self) -> str:
        return self.name


class Course(models.Model):
    """Курс: название и связь со студентами (M2M)."""

    name = models.TextField()
    students = models.ManyToManyField("Student", blank=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self) -> str:
        return self.name
