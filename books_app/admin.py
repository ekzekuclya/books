from django.contrib import admin
from .models import Book, Genre, Publisher, Comment, Like


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "amount_pages", "author", "publisher", "is_deleted"]
    list_filter = ["title", "is_deleted"]


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'address', 'website', 'publication_date', 'is_deleted']
    list_filter = ['name', 'country', 'address', 'publication_date', 'is_deleted']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'book']
    list_filter = ['content']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['book', 'user']
    list_filter = ['user']