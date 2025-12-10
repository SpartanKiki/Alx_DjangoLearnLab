# Delete the book
book = Book.objects.get(id=1)
book.delete()
# Expected output: (1, {'bookshelf.Book': 1})
