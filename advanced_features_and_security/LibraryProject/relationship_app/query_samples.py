from .models import Author, Book,Library,Librarian


library = Library.objects.get(name=library_name)
books = library.books.all()

author = Author.objects.get(name=author_name)
all_books = Book.objects.filter(author=author)

librarian = Librarian.objects.get(library=library)