# Update the book title
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
# Expected output: None (but the title is updated)
