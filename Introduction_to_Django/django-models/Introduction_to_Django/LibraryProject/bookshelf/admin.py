from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns to display
    search_fields = ('title', 'author')                     # search box
    list_filter = ('publication_year',)                     # filter sidebar

admin.site.register(Book, BookAdmin)
