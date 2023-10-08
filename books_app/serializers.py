from rest_framework import serializers
from .models import Genre, Publisher, Book, Comment, Like
from django.contrib.auth.models import User


class GenreSerializer(serializers.ModelSerializer):
    count_books = serializers.IntegerField(read_only=True)

    class Meta:
        model = Genre
        fields = ['id', 'title', 'count_books']


class PublisherSerializer(serializers.ModelSerializer):
    count_books = serializers.IntegerField(read_only=True)

    class Meta:
        model = Publisher
        fields = ['id', 'created_at', 'updated_at', 'publication_date', 'name',
                  'address', 'country', 'website', 'count_books']


class BookSerializer(serializers.ModelSerializer):
    count_likes = serializers.IntegerField(read_only=True)

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['genre'] = GenreSerializer(instance=instance.genre.all(), many=True).data
        res['publisher'] = PublisherSerializer(instance=instance.publisher).data
        return res

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'genre',
                  'amount_pages', 'created_at', 'updated_at', 'publisher', 'count_likes']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'book', 'user', 'content']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'book', 'user']
