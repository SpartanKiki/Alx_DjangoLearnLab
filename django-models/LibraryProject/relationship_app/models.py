from django.db import models

# Author model
# One author can write many books
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model
# Each book belongs to ONE author (ForeignKey)
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )

    def __str__(self):
        return self.title


# Library model
# A library can have MANY books and a book can be in MANY libraries
class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name


# Librarian model
# Each library has ONE librarian and each librarian manages ONE library
class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(
        Library,
        on_delete=models.CASCADE,
        related_name='librarian'
    )

    def __str__(self):
        return self.name
