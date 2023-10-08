from django.contrib import admin
from .models import SignupInfo
# Register your models here.


@admin.register(SignupInfo)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['user', 'info']
