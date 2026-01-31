"""
Тесты API курсов: retrieve, list, фильтрация по id и name, create, update, delete.

Все тесты явно проверяют код ответа и используют @pytest.mark.django_db.
"""
import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from students.models import Course


@pytest.mark.django_db
def test_course_retrieve(api_client, course_factory) -> None:
    """
    Проверка получения одного курса (retrieve).
    Создаём курс через фабрику, запрашиваем по id, проверяем, что вернулся тот же курс.
    """
    course = course_factory()
    url = reverse("courses-detail", args=[course.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["id"] == course.id
    assert response.data["name"] == course.name


@pytest.mark.django_db
def test_course_list(api_client, course_factory) -> None:
    """
    Проверка получения списка курсов (list).
    Создаём курсы через фабрику, запрашиваем список, проверяем результат.
    """
    course1 = course_factory()
    course2 = course_factory()
    url = reverse("courses-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    # Без пагинации response.data — список; с пагинацией — словарь с ключом "results"
    data = response.data if not isinstance(response.data, dict) else response.data.get("results", [])
    ids = [item["id"] for item in data]
    assert course1.id in ids
    assert course2.id in ids


@pytest.mark.django_db
def test_course_list_filter_by_id(api_client, course_factory) -> None:
    """
    Проверка фильтрации списка курсов по id.
    Создаём несколько курсов, передаём id одного в фильтр, проверяем один результат.
    """
    course_factory()
    target = course_factory()
    course_factory()
    url = reverse("courses-list")
    response = api_client.get(url, data={"id": target.id})
    assert response.status_code == status.HTTP_200_OK
    results = response.data if not isinstance(response.data, dict) else response.data.get("results", [])
    assert len(results) == 1
    assert results[0]["id"] == target.id


@pytest.mark.django_db
def test_course_list_filter_by_name(api_client, course_factory) -> None:
    """
    Проверка фильтрации списка курсов по name (подстрока).
    Создаём курсы с разными именами, фильтруем по части имени.
    """
    course_factory(name="Python для начинающих")
    course_factory(name="Java Advanced")
    course_factory(name="Python в вебе")
    url = reverse("courses-list")
    response = api_client.get(url, data={"name": "Python"})
    assert response.status_code == status.HTTP_200_OK
    results = response.data if not isinstance(response.data, dict) else response.data.get("results", [])
    assert len(results) == 2
    for item in results:
        assert "Python" in item["name"]


@pytest.mark.django_db
def test_course_create_success(api_client) -> None:
    """
    Тест успешного создания курса.
    Отправляем JSON с name (и при необходимости students), проверяем 201 и данные.
    """
    url = reverse("courses-list")
    payload = {"name": "Новый курс"}
    response = api_client.post(url, data=payload, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["name"] == payload["name"]
    assert "id" in response.data
    assert Course.objects.filter(name=payload["name"]).exists()


@pytest.mark.django_db
def test_course_update_success(api_client, course_factory) -> None:
    """
    Тест успешного обновления курса.
    Создаём курс через фабрику, обновляем через PATCH/PUT с JSON.
    """
    course = course_factory(name="Старое имя")
    url = reverse("courses-detail", args=[course.id])
    payload = {"name": "Обновлённое имя"}
    response = api_client.patch(url, data=payload, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == payload["name"]
    course.refresh_from_db()
    assert course.name == payload["name"]


@pytest.mark.django_db
def test_course_delete_success(api_client, course_factory) -> None:
    """
    Тест успешного удаления курса.
    Создаём курс через фабрику, удаляем через DELETE, проверяем 204 и отсутствие в БД.
    """
    course = course_factory()
    url = reverse("courses-detail", args=[course.id])
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Course.objects.filter(id=course.id).exists()
