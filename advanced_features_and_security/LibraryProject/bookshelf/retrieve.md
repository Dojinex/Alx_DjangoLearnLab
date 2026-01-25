# Retrieve Operation

## Command
To retrieve and display all attributes of the book with the title "1984", author "George Orwell", and publication year 1949 that you just created, execute the following command in the Django shell:

```python
from bookshelf.models import Book
book = Book.objects.get(title='1984', author="George Orwell", publication_year=1949)
print(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")
