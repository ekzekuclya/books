# from django.test import TestCase
# from .models import Book
# from datetime import datetime, timedelta

# Create your tests here.
# @api_view(['GET', 'POST'])
# def books_list(request):
#     if request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return response.Response(data=serializer.data, status=201)
#         raise ValidationError(serializer.errors)
#
#     else:
#         books = Book.objects.all()
#         serializer = BookSerializer(instance=books, many=True)
#         return response.Response(data=serializer.data, status=200)

 # @api_view(['GET', 'POST'])
# def genre_list(request):
#     if request.method == 'POST':
#         serializer = GenreSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return response.Response(data=serializer.data, status=201)
#         raise ValidationError(serializer.errors)
#     else:
#         genres = Genre.objects.all()
#         serializer = GenreSerializer(instance=genres, many=True)
#         return response.Response(data=serializer.data, status=200)

# @api_view(['GET', 'POST'])
# def publisher_list(request):
#     if request.method == 'POST':
#         serializer = PublisherSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return response.Response(data=serializer.data, status=201)
#         raise ValidationError(serializer.errors)
#     else:
#         publisher = Publisher.objects.all()
#         serializer = PublisherSerializer(instance=publisher, many=True)
#         return response.Response(data=serializer.data, status=200)

# @api_view(['GET', 'PUT', 'PATCH'])
# def books_pk(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#
#     if request.method in ['PUT', 'PATCH']:
#         serializer = BookSerializer(instance=book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return response.Response(data=serializer.data, status=201)
#         raise ValidationError(serializer.errors)
#
#     serializer = BookSerializer(instance=book)
#     return response.Response(data=serializer.data, status=200)

# @api_view(['GET'])
# def genres_pk(request, pk):
#     genre = get_object_or_404(Genre, pk=pk)
#     serializer = BookSerializer(instance=genre)
#     return response.Response(data=serializer.data, status=200)

# @api_view(['GET', 'PUT', 'PATCH'])
# def publisher_pk(request, pk):
#     publisher = get_object_or_404(Publisher, pk=pk)
#
#     if request.method in ['PUT', 'PATCH']:
#         serializer = PublisherSerializer(instance=publisher, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return response.Response(data=serializer.data, status=201)
#         raise ValidationError(serializer.errors)
#
#     serializer = PublisherSerializer(instance=publisher)
#     return response.Response(data=serializer.data, status=200)


"""
1) Достать все книги
2) Достать книгу по ID
3) Достать книгу созданные за последние 2 дня
4) Достать книги обновленные за последние 2 дня
5) Обновить amount_of_page у книги по ID
6) Посчитать кол-во книг у всех изданий
"""

# # 1 Достать все книги
# books = Book.objects.all()
#
# # 2 Достать книгу по ID
# # book_id = models.Book.filter(id=?).first()
#
# # 3 Достать книгу созданные за последние 2 дня
# two_days = datetime.now() - timedelta(days=2)
# book_two_days = Book.filter(created_at__gte=two_days)
# print(book_two_days)
#
#
# class BookList(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class BookList(APIView):
#     def get(self, request):
#         books = Book.objects.all()
#         serializer = BookSerializer(instance=books, many=True)
#         return response.Response(data=serializer.data, status=200)
#
#     def post(self, request):
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return response.Response(data=serializer.data, status=201)
#         raise ValidationError(serializer.errors)
#
#
# class GenreList(generics.ListCreateAPIView):
#     queryset = Genre.objects.all()
#     serializer_class = GenreSerializer

    # def get(self, request, format=None):
    #     genres = Genre.objects.all()
    #     serializer = GenreSerializer(instance=genres, many=True)
    #     return response.Response(data=serializer.data, status=200)
    #
    # def post(self, request):
    #     serializer = GenreSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return response.Response(data=serializer.data, status=201)
    #     raise ValidationError(serializer.errors)


# class PublisherList(generics.ListCreateAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = PublisherSerializer

    # def get(self, request, format=None):
    #     publisher = Publisher.objects.all()
    #     serializer = PublisherSerializer(instance=publisher, many=True)
    #     return response.Response(data=serializer.data, status=200)
    #
    # def post(self, request, format=None):
    #     serializer = PublisherSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return response.Response(data=serializer.data, status=201)
    #     raise ValidationError(serializer.errors)


# class BookDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

    # def get(self, request, pk, format=None):
    #     book = get_object_or_404(Book, pk=pk)
    #     serializer = BookSerializer(instance=book)
    #     return response.Response(data=serializer.data, status=200)
    #
    # def put(self, request, pk, format=None):
    #     book = get_object_or_404(Book, pk=pk)
    #     serializer = BookSerializer(instance=book, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return response.Response(data=serializer.data, status=200)
    #     raise ValidationError(serializer.errors)
    #
    #
    # def patch(self, request, pk, format=None):
    #     book = get_object_or_404(Book, pk=pk)
    #     serializer = BookSerializer(instance=book, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return response.Response(data=serializer.data, status=200)
    #     raise ValidationError(serializer.errors)
    #
    # def delete(self, request, pk, format=None):
    #     book = get_object_or_404(Book, pk=pk)
    #     book.delete()
    #     return response.Response(status=204)


# class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Genre.objects.all()
#     serializer_class = GenreSerializer

    # def get(self, request, pk, format=None):
    #     genre = get_object_or_404(Genre, pk=pk)
    #     serializer = BookSerializer(instance=genre)
    #     return response.Response(data=serializer.data, status=200)
    #
    # def delete(self, request, pk, format=None):
    #     genre = get_object_or_404(Book, pk=pk)
    #     genre.delete()
    #     return response.Response(status=204)

#
# class PublisherDetail(generics.RetrieveUpdateAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = PublisherSerializer

    # def get(self, request, pk, format=None):
    #     publisher = get_object_or_404(Publisher, pk=pk)
    #     serializer = PublisherSerializer(instance=publisher)
    #     return response.Response(data=serializer.data, status=200)
    #
    # def put(self, request, pk, format=None):
    #     publisher = get_object_or_404(Publisher, pk=pk)
    #     serializer = PublisherSerializer(instance=publisher, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return response.Response(data=serializer.data, status=201)
    #     raise ValidationError(serializer.errors)
    #
    #
    # def patch(self, request, pk, format=None):
    #     publisher = get_object_or_404(Publisher, pk=pk)
    #     serializer = PublisherSerializer(instance=publisher, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return response.Response(data=serializer.data, status=201)
    #     raise ValidationError(serializer.errors)

    # class BookSerializer(serializers.Serializer):
    #     id = serializers.IntegerField(read_only=True)
    #     created_at = serializers.DateTimeField(read_only=True)
    #     updated_at = serializers.DateTimeField(read_only=True)
    #     author = serializers.CharField(max_length=100)
    #     title = serializers.CharField(max_length=250)
    #     description = serializers.CharField()
    #     genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)
    #     publisher = serializers.PrimaryKeyRelatedField(queryset=Publisher.objects.all())
    #     amount_pages = serializers.IntegerField(min_value=1)
    #
    #     def create(self, validated_data):
    #         genre_list = validated_data.pop('genre')
    #         book = Book.objects.create(**validated_data)
    #         book.genre.add(*genre_list)
    #         return book
    #
    #     def update(self, instance, validated_data):
    #         instance.title = validated_data.get('title', instance.title)
    #         instance.author = validated_data.get('author', instance.author)
    #         instance.description = validated_data.get('description', instance.description)
    #         instance.amount_pages = validated_data.get('amount_pages', instance.amount_pages)
    #         instance.publisher = validated_data.get('publisher', instance.publisher)
    #
    #         instance.save()
    #         if 'genre' in validated_data:
    #             genre_list = validated_data['genre']
    #             instance.genre.clear()  # Очищаем текущие связи с жанрами
    #             instance.genre.add(*genre_list)
    #
    #         return instance

import random
import string
# data = {
#         "author":
#             "Zhanna"
#         ,
#         "title":
#             "Super MAMA"
#         ,
#         "description":
#             "YA JE MAT"
#         ,
#         "genre": [1]
#         ,
#         "publisher":
#             1
#         ,
#         "amount_pages":
#             1
#
#     }
# print(data)
#
# def generate_word(n):
#     word = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))
#     return word
#
#
# def generate_text(n):
#     text = ''
#     while len(text) < n:
#         b = random.randint(4, 8)
#         if len(text) + b <= n:
#             text += generate_word(b)
#             text += ' '
#     return text
#
#
# a = generate_text(20)
# print(a)
# a = [random.randint(1, 2) for i in range(random.randint(1, 2))]
# print(a)

# genre_ids = self.request.query_params.get('genre')
# publisher_id = self.request.query_params.get('publisher')

# if genre_ids:
#     genre_id_list = [int(i) for i in genre_ids.split(',')]
#     qs = qs.filter(genre__id__in=genre_id_list)
#
# if publisher_id:
#     publisher_id_list = [int(i) for i in publisher_id.split(',')]
#     qs = qs.filter(publisher__id__in=publisher_id_list)

#
# from .models import Comment
#
# comm = Comment.objects.all()
# print(comm)
from rest_framework.test import APITestCase
from .models import Book, Genre
from django.urls import reverse
from django.contrib.auth.models import User


# написать юнит тесты для
'''BookViewSet:

a. Проверка стандартного поведения:
- Получить список всех книг.
- Получить детали одной книги.
- Создать новую книгу.
- Обновить существующую книгу.
- Удалить книгу (используя мягкое удаление).


b. Проверка фильтрации:
- Применить фильтры для списка книг и убедиться, что они работают корректно.


c. Проверка метода likes:
- Получить список книг, отсортированный по количеству лайков.


d. Проверка мягкого удаления:
- Удалить книгу и убедиться, что ее is_deleted стало True.
- Попытаться получить удаленную книгу из общего списка и удостовериться, что ее нет.'''


class BookViewTestCase(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='test_username',
                                             email='alex123@gmail.com',
                                             password='super_password2020',
                                             )
        self.client.force_authenticate(user=self.user)
        genre = Genre.objects.create(title='Action')
        self.book = Book.objects.create(**{'author': 'Shabinio',
                'title': 'Yes please',
                'description': 'Opisanie',
                'amount_pages': 128493,

        })


    def test_get_books(self):
        url = reverse('books-list')
        response = self.client.get(url)
        print(response)

    def test_book(self):
        genre = Genre.objects.create(title='Drama')
        url = reverse('books-list')
        data = {'author': 'Shabinio',
                'title': 'Yes please',
                'description': 'Opisanie',
                'amount_pages': 128493,
                'genre': genre.id,
        }
        response = self.client.post(url, data=data)
        book = Book.objects.get(id=response.data['id'])

        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.data['author'], book.author)

    def test_filter(self):

        url = reverse('books-list')
        response = self.client.get(url + '?author=Shabinio')
        print(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['Shabinio'], 'Shabinio')

    def test_likes(self):
        url = reverse('books-most-liked')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_delete_and_get(self):
        url = reverse('books-detail', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEquals(response.status_code, 204)
        book = Book.objects.filter(id=self.book.id).first()
        self.assertTrue(book.is_deleted)











