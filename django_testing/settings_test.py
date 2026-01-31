"""
Настройки Django для тестов (pytest) и для запуска сервера без PostgreSQL.

Для pytest используется SQLite в памяти.
Для ручной проверки API (runserver) задайте USE_SQLITE_FILE=1 —
тогда используется файл test_db.sqlite3 в корне проекта.
"""
import os

from django_testing.settings import *  # noqa: F401, F403

if os.environ.get("USE_SQLITE_FILE"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "test_db.sqlite3",  # noqa: F405
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        }
    }
