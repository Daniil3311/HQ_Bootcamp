from django_filters import rest_framework as filters
from app.models import Lesson


class LessonFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Lesson
        fields = '__all__'