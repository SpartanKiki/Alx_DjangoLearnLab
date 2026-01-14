from .forms import ExampleForm
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    return render(request, 'bookshelf/form_example.html')


@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'bookshelf/form_example.html', {'book': book})


@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return render(request, 'bookshelf/book_list.html')
