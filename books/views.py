import requests, os
from django.shortcuts import render
from django.views.generic import ListView, DetailView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from books.models import Book, Profile
from reports.models import Report

# Create your views here.
class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "books/book_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_instance = Profile.objects.get(user=self.request.user)
        context["favorite_books"] = profile_instance.favorite_books.all()
        context["read_later_books"] = profile_instance.read_later_books.all()
        return context

class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reports"] = Report.objects.filter(book=self.object).order_by("-created_at")
        return context

class BookSearchView(ListView):
    model = Book
    context_object_name = "books"
    template_name = "books/book_search.html"

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     search_query = self.request.GET.get("search", None)
    #     if search_query:
    #         queryset = queryset.filter(title__icontains=search_query)
    #     return queryset

    def get_queryset(self):
        query = self.request.GET.get("query", '')
        if query:
            api_key = os.environ.get("GOOGLE_API_KEY") # GOOGLE_API_KEY
            url = "https://www.googleapis.com/books/v1/volumes"
            params = {
                'q': query,
                "printType": "books",
                "maxResults": 10,
                "key": api_key,
            }
            response = requests.get(url, params=params)
            if response.status_code == 200:
                print(response.json().get("items", [])[0])
                return response.json().get("items", [])
        return []
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("query", '')
        return context

class AddToFavoritesView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        book = Book.objects.get(pk=kwargs["pk"])
        self.request.user.profile.favorite_books.add(book)
        return reverse_lazy("books:book-detail", kwargs={"pk": kwargs["pk"]})

class AddToReadLaterView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        book = Book.objects.get(pk=kwargs["pk"])
        self.request.user.profile.read_later_books.add(book)
        return reverse_lazy("books:book-detail", kwargs={"pk": kwargs["pk"]})
