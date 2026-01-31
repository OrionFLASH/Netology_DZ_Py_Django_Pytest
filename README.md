# Учебный Django-проект: тестирование API (Нетология)

Учебный Django-проект с одним заданием: **тестирование API курсов и студентов** (pytest, pytest-django, model_bakery). Реализация размещена в корне проекта без дополнительного деления по подкаталогам заданий.

## Структура проекта

- **Корень** — Django-проект: `manage.py`, настройки в `django_testing/`, маршрутизация в `django_testing/urls.py`.
- **students** — приложение: модели `Course` и `Student`, API курсов (DRF ViewSet), фильтры по `id` и `name`.
- **tests** — тесты pytest: фикстуры в `tests/conftest.py`, тесты API курсов в `tests/students/test_courses_api.py`.
- **Docs** — исходные материалы задания: формулировка и требования в `Docs/README_исходное_задание.md`.

## Назначение

Бэкенд приложения с курсами и студентами уже реализован в заготовке; в проекте добавлены тесты для API курсов: получение одного курса, списка, фильтрация по `id` и `name`, создание, обновление и удаление. Используются фикстуры для API-клиента и фабрик курсов/студентов (model_bakery).

## Установка и запуск

1. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   # или: venv\Scripts\activate  (Windows)
   ```

2. Установите зависимости (в т.ч. для тестов):
   ```bash
   pip install -r requirements-dev.txt
   ```

3. Для **запуска тестов** отдельная база не нужна: pytest использует настройки `django_testing.settings_test` (SQLite в памяти):
   ```bash
   pytest
   ```

4. Для **запуска сервера разработки**:
   - **С PostgreSQL:** создайте базу `netology_django_testing`, выполните `python manage.py migrate` и `python manage.py runserver`.
   - **Без PostgreSQL (проверка API):** используйте файловую SQLite:
   ```bash
   USE_SQLITE_FILE=1 DJANGO_SETTINGS_MODULE=django_testing.settings_test python manage.py migrate
   USE_SQLITE_FILE=1 DJANGO_SETTINGS_MODULE=django_testing.settings_test python manage.py runserver
   ```
   - API курсов: <http://127.0.0.1:8000/api/v1/courses/>  
   - Админка: <http://127.0.0.1:8000/admin/>

## Основные сценарии тестирования

- **Получение одного курса (retrieve)** — создаётся курс через фабрику, запрос по id, проверка кода 200 и совпадения данных.
- **Список курсов (list)** — создаются несколько курсов, запрос списка, проверка кода 200 и наличия созданных курсов в ответе.
- **Фильтрация по id** — создаются несколько курсов, в запрос передаётся id одного, проверка одного элемента в ответе и кода 200.
- **Фильтрация по name** — создаются курсы с разными именами, фильтр по подстроке имени, проверка кода 200 и состава списка.
- **Создание курса** — POST с JSON `{"name": "..."}`, проверка 201 и появления записи в БД.
- **Обновление курса** — курс создаётся фабрикой, PATCH с новым именем, проверка 200 и обновлённых данных.
- **Удаление курса** — курс создаётся фабрикой, DELETE, проверка 204 и отсутствия записи в БД.

Во всех тестах явно проверяется код ответа; используется декоратор `@pytest.mark.django_db`.

## Переменные и функции (кратко)

- **Фикстуры (tests/conftest.py)**  
  - `api_client` — экземпляр `rest_framework.test.APIClient`.  
  - `course_factory` — фабрика курсов через `model_bakery.baker.make(Course, **kwargs)`.  
  - `student_factory` — фабрика студентов через `baker.make(Student, **kwargs)`.

- **Модели (students/models.py)**  
  - `Student`: `name` (TextField), `birth_date` (DateField, null=True).  
  - `Course`: `name` (TextField), `students` (ManyToManyField к Student).

- **API**  
  - Эндпоинты курсов: список `GET /api/v1/courses/`, детали `GET/PUT/PATCH/DELETE /api/v1/courses/<id>/`, создание `POST /api/v1/courses/`.  
  - Параметры фильтрации: `id`, `name` (подстрока).

## История версий

- **0.1** — Инициализация проекта по заданию Нетологии 3.4-django-testing: структура Django, приложение students, фикстуры и тесты API курсов (retrieve, list, фильтры по id и name, create, update, delete); настройки для тестов на SQLite, README и Docs.
