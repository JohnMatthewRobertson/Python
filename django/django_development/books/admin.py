"""TODO"""
from django.contrib import admin
from books.models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    """TODO"""
    list_display = ("title", "author", "price",)

admin.site.register(Book, BookAdmin)
