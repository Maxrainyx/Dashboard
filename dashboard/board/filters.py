from django_filters import FilterSet, DateFromToRangeFilter, CharFilter
from .models import Comment


# Создаем свой набор фильтров для модели Post.
class CommentFilter(FilterSet):
    class Meta:
        model = Comment
        fields = {
            'post__title': ['contains'],
        }

