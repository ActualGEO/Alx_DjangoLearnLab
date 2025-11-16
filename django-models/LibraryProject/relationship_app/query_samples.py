from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        if books.exists():
            for book in books:
                print(f"{book.title}")
            else:
                print("No book found for this author.")


    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found")



def list_all_books_in_a_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        if books.exists():
            for book in books:
                print(f"{book.title} by {book.author.name}")
        else:
            print("This library has no books.")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")



def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.Librarian
        print(f"Librarian: {Librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found")



if __name__ == "__main__":
    query_books_by_author("George")


