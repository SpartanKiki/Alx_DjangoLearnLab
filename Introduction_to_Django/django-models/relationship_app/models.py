from django.db import models

# Author model
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Book model
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField(null=True, blank=True)  # optional field

    def __str__(self):
        return self.title

# Library model
class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return self.name

# Librarian model
class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
