## CRUD OPERATIONS

```from bookshelf.models import Book```

### Create Book

```py
book = Book.objects.create(title="The gods are not to blame", author="Ola Rotimi",publication_year=2005)
```

output:
```sh
<Book: Book object (4)>
```

### Retrieve Book

```py
Book.objects.get(title="1984")
```
### Update Book

```py
book.title = “Nineteen Eighty-Four”
book.save()
```

### Delete Book
```py
book.delete()
```
output:
```sh
output:
(1, {'bookshelf.Book': 1})
```