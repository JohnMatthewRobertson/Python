"""TODO"""
from django.views.generic import ListView, DetailView
from books.models import Book


# Create your views here.

class BookListView(ListView):
    """TODO"""
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'

class BookDetailView(DetailView):
    """TODO"""
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
