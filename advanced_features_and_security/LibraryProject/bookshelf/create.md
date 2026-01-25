# Create Operation

## Command
To create a new book entry in the database, execute the following command in the Django shell:

```python
from bookshelf.models import Book
b1 = Book.objects.create(title='1984', author="George Orwell", publication_year=1949)

Book object (2)
