"""
Фильтры для API курсов: по id и по name.
"""
from django_filters import CharFilter, FilterSet, ModelMultipleChoiceFilter

from students.models import Course


class CourseFilter(FilterSet):
    """Фильтр курсов: id (множественный выбор) и name (поиск по строке)."""

    id = ModelMultipleChoiceFilter(
        field_name="id",
        to_field_name="id",
        queryset=Course.objects.all(),
    )
    name = CharFilter(lookup_expr="icontains")

    class Meta:
        model = Course
        fields = ("id", "name")
