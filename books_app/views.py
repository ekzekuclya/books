from rest_framework import response, status, generics, viewsets, filters
from rest_framework.validators import ValidationError
from .models import Book, Genre, Publisher, Comment, Like
from .serializers import BookSerializer, GenreSerializer, PublisherSerializer, LikeSerializer, CommentSerializer
from .utils import generate_data
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BookFilter, PublisherFilter
from django.db.models import Count, Avg
from rest_framework.decorators import action
from openpyxl import Workbook
from rest_framework.permissions import AllowAny


class BookListViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    filterset_class = BookFilter
    permission_classes = [AllowAny]  # Исключение
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering = ['created_at']
    search_fields = ['title', 'description', 'genre__title', 'publisher__name', 'author']

    def get_queryset(self):
        qs = Book.objects.all().select_related('publisher').prefetch_related('genre')
        qs = qs.filter(is_deleted=False)
        return qs

    def destroy(self, request, *args, **kwargs):
        book = self.get_object()
        book.is_deleted = True
        book.save(update_fields=['is_deleted'])
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['get'], detail=True, url_path='count-g')
    def count_genres(self, request, pk=None):
        book = self.get_object()
        count = book.genre.count()
        return response.Response({'count_genres': count})

    @action(methods=['get'], detail=False, url_path='count-del')
    def count_deleted_books(self, request):
        book = Book.objects.all()
        amount = book.filter(is_deleted=True).count()
        return response.Response({'count_deleted_books': amount})

    @action(methods=['post'], detail=True, url_path='add-genre')
    def add_genre(self, request, pk):
        book = self.get_object()
        if request.data.get('genre_id'):
            book.genre.add(request.data.get('genre_id'))
            return response.Response(status=status.HTTP_202_ACCEPTED)
        return response.Response("type genre_id")

    @action(methods=['get'], detail=False, url_path='export-excel')
    def export_excel(self, request, pk=None):
        books = Book.objects.all()

        wb = Workbook()
        ws = wb.active

        headers = ['Author', 'title', 'description', 'amount_pages', 'is_deleted', 'genre', 'publisher']
        ws.append(headers)

        for book in books:
            genre_data = ''.join(f'{genre.id}, {genre.title}' for genre in Genre.objects.all())
            publisher_data = ''.join(f'{publisher.name}, {publisher.country}' for publisher in Publisher.objects.all())

            ws.append([book.author, book.title, book.description,
                       book.amount_pages, book.is_deleted, genre_data, publisher_data])
        wb.save('books.xlsx')

        return response.Response('OK')

    # @action(methods=['post', 'patch'], detail=True, url_path='add-comment')
    # def add_comment(self, request, pk):
    #     user = self.request.user
    #     book = self.get_object()
    #     if request.data:
    #         content = request.data['content']
    #         if request.method == 'POST':
    #             comm = Comment.objects.create(content=content, book=book, user=user)
    #             return response.Response({'user': user.username, 'content': comm.content}, status=status.HTTP_201_CREATED)
    #             # if request.method == 'PATCH':
    #             #     comment = Comment.objects.get(book=book, user=user, content=request.data['content'])
    #             #     comment.content = content
    #             #     comment.save()
    #
    #         return response.Response(status=status.HTTP_400_BAD_REQUEST)
    #     return response.Response(status=status.HTTP_401_UNAUTHORIZED)

    @action(methods=['get'], detail=False, url_path='most-liked')
    def most_liked(self, request):
        queryset = Book.objects.all().annotate(count_likes=Count('like')).order_by('-count_likes')
        return response.Response(BookSerializer(queryset, many=True).data)


class GenreListAPIView(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    ordering = ['title']

    @action(methods=['get'], detail=False, url_path='popular-genre')
    def popular_genre(self, request):
        queryset = Genre.objects.all().annotate(count_books=Count('book')).order_by('-count_books')[:3]
        return response.Response(GenreSerializer(queryset, many=True).data)

    @action(methods=['get'], detail=True, url_path='avg-pages')
    def average_pages(self, request, pk):
        genre = self.get_object()
        avg_pages = Book.objects.filter(genre=genre).aggregate(avg=Avg('amount_pages'))
        return response.Response({'avg_pages': avg_pages['avg']})


class PublisherListViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    filterset_class = PublisherFilter
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering = ['name']

    @action(methods=['get'], detail=False, url_path='popular-pub')
    def popular_publishers(self, request):
        qs = Publisher.objects.all().annotate(count_books=Count('book')).order_by('-count_books')[:3]
        return response.Response(PublisherSerializer(qs, many=True).data)

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(is_deleted=False)
        return qs

    def destroy(self, request, *args, **kwargs):
        publisher = self.get_object()
        publisher.is_deleted = True
        publisher.save(update_fields=['is_deleted'])
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class GenerateBook(generics.CreateAPIView):
    serializer_class = BookSerializer

    def get(self, request, format=None):
        data = generate_data()
        serializer = BookSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(data=serializer.data, status=201)
        raise ValidationError(serializer.errors)


class BookCommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = None

    def get_queryset(self):
        book_id = self.kwargs['book_pk']  # Получаем идентификатор книги из роутера
        return Comment.objects.filter(book_id=book_id)

    def perform_create(self, serializer):
        book_id = self.kwargs['book_pk']
        book = Book.objects.get(id=book_id)
        serializer.save(user=self.request.user, book=book)


    # @action(methods=['post', 'patch'], detail=False, url_path='add-comment')
    # def add_comment(self, request, book_pk):
    #     user = self.request.user
    #     if self.request.data:
    #         content = self.request.data['content']
    #         if self.request.method == 'POST':
    #             comm = Comment.objects.create(content=content, book_id=book_pk, user=user)
    #             return response.Response({'user': user.username, 'content': comm.content},
    #                                      status=status.HTTP_201_CREATED)

    # @action(methods=['delete'], detail=True, url_path='delete-comment')
    # def delete_comment(self, request, pk):
    #     comment = self.get_object()
    #     comment.delete()
    #     return response.Response(status=status.HTTP_204_NO_CONTENT)

# class BookCommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     pagination_class = None
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         book_id = self.kwargs['book_pk']
#         return qs.filter(book_id=book_id)


class BookLikeAPIView(viewsets.ModelViewSet):
    serializer_class = LikeSerializer

    def get_queryset(self):
        return Like.objects.filter(book_id=self.kwargs['book_pk'])

    @action(methods=['post'], detail=False, url_path='add-like')
    def add_like(self, request, book_pk):
        if Book.objects.filter(id=book_pk):
            like, created = Like.objects.get_or_create(user=self.request.user, book_id=book_pk)
            if created:
                return response.Response(status=status.HTTP_200_OK)
            else:
                return response.Response({'detail': 'ты уже лайкал'})
        else:
            return response.Response({'detail': 'книга не найдена'},status=status.HTTP_404_NOT_FOUND)

    @action(methods=['delete'], detail=False, url_path='remove-like')
    def delete_like(self, request, book_pk):
        if Book.objects.filter(id=book_pk):
            like = Like.objects.filter(book_id=book_pk, user=request.user).first()
            if like:
                like.delete()
                return response.Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return response.Response({'Detail': 'нет лайка'})
        else:
            return response.Response({'detail': 'книга не найдена'}, status=status.HTTP_404_NOT_FOUND)
















