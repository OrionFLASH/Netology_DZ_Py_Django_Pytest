#!/usr/bin/env python
"""
Точка входа для утилит управления Django.
Используется для запуска миграций, сервера разработки и т.д.
"""
import os
import sys


def main() -> None:
    """Запуск команд Django из командной строки."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_testing.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
