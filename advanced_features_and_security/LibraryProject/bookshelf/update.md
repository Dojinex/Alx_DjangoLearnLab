# Update Operation

## Command
To update the title of the book originally titled "1984" to "Nineteen Eighty-Four" and save the changes, execute the following command in the Django shell:

```python
from bookshelf.models import Book
book = Book.objects.get(title='1984', author="George Orwell", publication_year=1949)
book.title = 'Nineteen Eighty-Four'
book.save()b1