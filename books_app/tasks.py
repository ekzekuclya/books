
import datetime
from django.conf import settings
from celery import app
from django.core.mail import send_mail, EmailMessage
from .models import Book, Genre, Publisher
from openpyxl import Workbook


@app.shared_task
def export_excel():
    today = datetime.datetime.today()
    last_week = today - datetime.timedelta(weeks=1)
    books = Book.objects.filter(created_at__gte=last_week)

    wb = Workbook()
    ws = wb.active

    headers = ['Author', 'title', 'description', 'amount_pages', 'is_deleted', 'genre', 'publisher', 'created_at']
    ws.append(headers)

    for book in books:
        genre_data = ''.join(f'{genre.id}, {genre.title}' for genre in Genre.objects.all())
        publisher_data = ''.join(f'{publisher.name}, {publisher.country}' for publisher in Publisher.objects.all())

        ws.append([book.author, book.title, book.description,
                   book.amount_pages, book.is_deleted, genre_data, publisher_data, str(book.created_at)])
    wb.save('books.xlsx')
    msg = EmailMessage('Sub', 'excel', settings.EMAIL_HOST_USER, ['ekzekuciya07@gmail.com'])
    msg.content_subtype = "html"
    msg.attach_file('books.xlsx')
    msg.send()


@app.shared_task
def send_email(subject, message, recipient_list):
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipient_list,
        fail_silently=False
    )


@app.shared_task
def send_statistics():
    swipe_in = datetime.datetime.today()
    new_swipe_in = (swipe_in - datetime.timedelta(minutes=2))

    books_in_last_2_mins = Book.objects.filter(created_at__gte=new_swipe_in,
                                               ).values_list('title', flat=True)

    subject = 'Book conun eken'
    message = f'Book aibai conun eken {books_in_last_2_mins}'
    recipient_list = ['ekzekuciya07@gmail.com']

    send_email(
        subject=subject,
        message=message,
        recipient_list=recipient_list)
