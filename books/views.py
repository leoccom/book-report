import requests
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from books.models import Book
from reports.models import Report

# Create your views here.
class BookListView(ListView):
    model = Book
    context_object_name = "books"
    template_name = "books/book_list.html"

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     search_query = self.request.GET.get("search", None)
    #     if search_query:
    #         queryset = queryset.filter(title__icontains=search_query)
    #     return queryset

    def get_queryset(self):
        query = self.request.GET.get("query", '')
        if query:
            api_key = "AIzaSyAntCwlh7Qnprgc4R33KZo0Fjkyf3L_3XU"
            url = "https://www.googleapis.com/books/v1/volumes"
            params = {
                'q': query,
                "printType": "books",
                "maxResults": 10,
                "key": api_key,
            }
            response = requests.get(url, params=params)
            if response.status_code == 200:
                return response.json().get("items", [])
        return []
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("query", '')
        return context

class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reports"] = Report.objects.filter(book=self.object).order_by("-created_at")
        return context