from relationship_app.models import Author, Book, Library, Librarian

def sample_queries():
    # Query all books by a specific author
    author = Author.objects.first()
    if author:
        books_by_author = Book.objects.filter(author=author)
        print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

    # List all books in a library
    library = Library.objects.first()
    if library:
        books_in_library = library.books.all()
        print(f"Books in library {library.name}: {[book.title for book in books_in_library]}")

    # Retrieve the librarian for a library
    if library and hasattr(library, 'librarian'):
        librarian = library.librarian
        print(f"Librarian of {library.name}: {librarian.name}")
