from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

# Author model
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book model
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # Custom validation: publication year cannot be in the future
    def clean(self):
        if self.publication_year > date.today().year:
            raise ValidationError("Publication year cannot be in the future.")
