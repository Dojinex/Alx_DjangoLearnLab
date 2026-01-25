# Delete Operation

## Command
To delete the book titled "Nineteen Eighty-Four" and confirm the deletion, execute the following command in the Django shell:

```python
from bookshelf.models import Book
book = Book.objects.get(title='Nineteen Eighty-Four', author="George Orwell", publication_year=1949)
book.delete()

# Confirming deletion by trying to retrieve all books
books = Book.objects.all()
print(books)