from django.urls import path
from .views import list_books, LibraryDetailView
from .views import list_books, LibraryDetailView, login_view, logout_view, register_view

urlspatterns = [
    path('books/', list_books, name='list_book'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='libary_view'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'), 


]