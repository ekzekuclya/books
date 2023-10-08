from django.db import models
import random
import string


class IsDeleted(models.Model):
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class TrackData(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def generate_word(n):
    word = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))
    return word


def generate_text(n):
    text = ''
    while len(text) < n:
        if len(text) <= n:
            text += generate_word(random.randint(4, 8))
            text += ' '
    return text


def generate_data():
    data = {
            "author":
                generate_word(random.randint(4,8)).capitalize()
            ,
            "title":
                generate_text(random.randint(6, 10)).capitalize()
            ,
            "description":
                generate_text(random.randint(10, 50)).capitalize()
            ,
            "genre": [random.randint(1, 2) for _ in range(random.randint(1, 2))]
            ,
            "publisher":
                random.randint(1, 3)
            ,
            "amount_pages":
                random.randint(100, 9999)
        }
    return data