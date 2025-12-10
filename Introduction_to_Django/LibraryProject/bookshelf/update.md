# Update the book title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
# Expected output: None (title updated)
