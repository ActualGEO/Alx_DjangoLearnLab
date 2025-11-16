from django.urls import path
from . import views

urlspatterns = [
    path('books/', views.list_book, name='list_book'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='libary_view'),


]