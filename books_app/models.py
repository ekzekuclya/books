from django.db import models
from .utils import TrackData, IsDeleted
from django.contrib.auth.models import User


class Genre(TrackData):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Publisher(TrackData, IsDeleted):
    publication_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=200)
    website = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(TrackData, IsDeleted):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=250)
    description = models.TextField()
    genre = models.ManyToManyField(Genre)
    amount_pages = models.PositiveSmallIntegerField()
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title+' '+self.author


class Comment(TrackData, IsDeleted):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return self.content


class Like(TrackData):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True, related_name='like')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)



