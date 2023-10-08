from .models import Book, Comment, Like
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .tasks import send_email


@receiver(post_save, sender=Book)
def send_email_books(sender, instance, created, **kwargs):
    if created:
        subject = 'Book created successfully'
        message = f'Ty sozdal topovyi books {instance.title}'
        recipient_list = ['ekzekuciya07@gmail.com']
        if instance.book.created_by.email:
            send_email.delay(subject=subject,
                                message=message,
                                recipient_list=recipient_list)


@receiver(post_save, sender=Book)
def update_amount_of_books(sender, instance, created, **kwargs):
    if created:
        instance.publisher.amount_of_books += 1
        instance.publisher.save()
    else:
        if instance.is_deleted:
            instance.publisher.amount_of_books -= 1
            instance.publisher.save()


@receiver(post_delete, sender=Book)
def update_amount_of_books_after_delete(sender, instance, **kwargs):
        instance.publisher.amount_of_books -= 1
        instance.publisher.save()


@receiver(post_save, sender=Comment)
def update_amount_of_comments(sender, instance, created, **kwargs):
    if created:
        instance.book.amount_of_comments += 1
        instance.book.save()
    else:
        if instance.is_deleted:
            instance.book.amount_of_comments -= 1
            instance.book.save()


@receiver(post_delete, sender=Comment)
def update_amount_of_comments_after_delete(sender, instance, **kwargs):
        instance.book.amount_of_comments -= 1
        instance.book.save()


@receiver(post_save, sender=Like)
def update_amount_of_likes(sender, instance, created, **kwargs):
    if created:
        instance.book.amount_of_likes += 1
        instance.book.save()
    else:
        if instance.is_deleted:
            instance.book.amount_of_likes -= 1
            instance.book.save()


@receiver(pre_save, sender=Like)
def prevent_likes(sender, instance, **kwargs):
    like = Like.objects.filter(user=instance.user, book=instance.book).first()
    if like:
        raise ValidationError('Вы уже ставили лайк для этой книги!!!')


@receiver(post_delete, sender=Like)
def update_amount_of_likes_after_delete(sender, instance, **kwargs):
        instance.book.amount_of_likes -= 1
        instance.book.save()