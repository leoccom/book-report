from django.shortcuts import render
from django.views.generic import ListView

from books.models import Book

# Create your views here.
class LibraryListView(ListView):
    model = Book
    context_object_name = "books"
    template_name = "library/library_list.html"