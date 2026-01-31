"""
Настройки Django для запуска тестов (pytest).

Используется SQLite в памяти, чтобы тесты можно было запускать без PostgreSQL.
"""
from django_testing.settings import *  # noqa: F401, F403

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
