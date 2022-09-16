"""TODO"""
from django.contrib import admin
from books.models import Book, Review

# Register your models here.

class ReviewInline(admin.TabularInline):
    """TODO"""
    model = Review

class BookAdmin(admin.ModelAdmin):
    """TODO"""
    inlines = [ReviewInline,]
    list_display = ("title", "author", "price",)

admin.site.register(Book, BookAdmin)
