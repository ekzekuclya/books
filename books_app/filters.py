from django_filters.rest_framework import FilterSet, NumberFilter, BaseInFilter, CharFilter
from .models import Book, Publisher
from django.db.models import Count


class CharInField(BaseInFilter, CharFilter):
    pass


class NumberInFilter(BaseInFilter, NumberFilter):
    pass


class BookFilter(FilterSet):
    publisher = NumberInFilter(field_name='publisher', lookup_expr='in')
    genre = NumberInFilter(field_name='genre', lookup_expr='in')
    title = CharInField(field_name='title', lookup_expr='in')
    author = CharInField(field_name='author', lookup_expr='in')
    popular_likes = NumberFilter(field_name='popular-likes', method='popular_books')

    @staticmethod
    def popular_books(self, queryset, _, value):
        return queryset.annotate(count_likes=Count('like')).order_by('count-likes')

        # def most_liked(self, request):
        #     queryset = Book.objects.all().annotate(count_likes=Count('like')).order_by('-count_likes')
        #     return response.Response(BookSerializer(queryset, many=True).data)

    class Meta:
        model = Book
        fields = ['genre', 'publisher', 'title', 'author', 'popular_likes']


class PublisherFilter(FilterSet):
    country = CharInField(field_name='country', lookup_expr='in')
    min_books = NumberFilter(field_name='book__id', method='filter_min_books')
    max_books = NumberFilter(field_name='book__id', method='filter_max_books')

    @staticmethod
    def filter_min_books(self, queryset, _, value):
        if value:
            return queryset.annotate(count_books=Count('book')).filter(count_books__gte=value)
        return queryset

    @staticmethod
    def filter_max_books(self, queryset, _, value):
        if value:
            return queryset.annotate(count_books=Count('book')).filter(count_books__lte=value)
        return queryset

    class Meta:
        model = Publisher
        fields = ['country', 'min_books', 'max_books']


class Popular:
    pass

