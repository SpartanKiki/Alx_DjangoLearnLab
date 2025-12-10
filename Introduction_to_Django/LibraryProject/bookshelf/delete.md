# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Expected output: (1, {'bookshelf.Book': 1})
