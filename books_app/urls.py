from .views import BookListViewSet, GenreListAPIView, PublisherListViewSet, GenerateBook, BookCommentViewSet, BookLikeAPIView
from django.urls import path, include
from rest_framework_nested import routers


router = routers.DefaultRouter()

router.register('books', BookListViewSet, basename='books')
router.register('genre', GenreListAPIView, basename='genre')
router.register('publisher', PublisherListViewSet, basename='publisher')

books_router = routers.NestedDefaultRouter(router, r'books', lookup='book')
books_router.register('comments', BookCommentViewSet, basename='books-comments')
books_router.register('likes', BookLikeAPIView, basename='likes')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(books_router.urls)),
    path('generate/', GenerateBook.as_view(), name='generate'),
]


