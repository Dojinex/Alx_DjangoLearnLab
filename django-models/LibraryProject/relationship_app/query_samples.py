from .models import Author, Book, Library, Librarian

# Add Author objects
chinua = Author.objects.create(name="Chinua Achebe")
chinua.save()
ama = Author.objects.create(name="Ama Ata Aidoo")
ama.save()
author_name = Author.objects.create(name='Author Name')

#Add Book objects
things = Book.objects.create(title="Things Fall Apart", author=chinua) 
dilemma = Book.objects.create(title="Dilemma of a Ghost", author=ama)

things.save()
dilemma.save()

# Get books by one author
Book.objects.get(author=ama) 
Book.objects.get(author=chinua)
Author.objects.get(name=author_name)
Author.objects.filter(author=author)

# List all books
Book.objects.all()

# Create Library Instance
balme = Library.objects.create(name='balme')
balme.save()

# Add books to Library
balme.books.add(things, dilemma)

# List all books in Library
balme.books.all()
Library.objects.get(name=library_name)

# Add Librarian
agyim = Librarian.objects.create(name='Agyim Taala', library=balme)
agyim.save()

#Retrieve a Libryrian for a library
agyim.library
Librarian.objects.get(library=balme)

