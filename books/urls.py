from django.urls import path
from .views import BookListView, BookDetailView, BookSearchView, AddToFavoritesView, AddToReadLaterView

app_name = "books"
urlpatterns = [
    path('', BookListView.as_view(), name="book-list"),
    path("<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("<int:pk>/add-to-favorites/", AddToFavoritesView.as_view(), name="add-to-favorites"),
    path("<int:pk>/add-to-read-later/", AddToReadLaterView.as_view(), name="add-to-read-later"),
    path("search/", BookSearchView.as_view(), name="book-search"),
]