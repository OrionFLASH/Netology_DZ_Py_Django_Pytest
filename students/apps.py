from django.apps import AppConfig


class StudentsConfig(AppConfig):
    """Конфигурация приложения students."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "students"
    verbose_name = "Студенты и курсы"
