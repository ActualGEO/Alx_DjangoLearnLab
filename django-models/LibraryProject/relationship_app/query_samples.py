from relationship_app.models import Author, Book, Library, Librarian

author = Author.objects.get(name='Desmond')
books_by_author = author.books.all()

library = Library.objects.get(name='Central')
library_books = Library.books.all()

librarian = library.librarian