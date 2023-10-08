# Generated by Django 4.2.4 on 2023-08-24 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0010_remove_book_comment_book_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books_app.book'),
        ),
    ]
