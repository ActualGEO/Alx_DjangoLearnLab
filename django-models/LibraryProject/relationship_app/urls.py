from django.urls import path
from .views import list_books, LibraryDetailView

urlspatterns = [
    path('books/', list_books, name='list_book'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='libary_view'),


]