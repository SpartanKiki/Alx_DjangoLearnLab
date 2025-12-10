# Retrieve the book we created
book = Book.objects.get(title="1984")
book
# Expected output: <Book: Book object (1)>
