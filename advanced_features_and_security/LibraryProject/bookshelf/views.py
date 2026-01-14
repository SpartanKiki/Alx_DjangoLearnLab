from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from .models import Book

@csrf_protect
def book_list(request):
    """
    Secure view:
    - Uses Django ORM (prevents SQL injection)
    - CSRF protected
    - Safe rendering
    """

    query = request.GET.get("q", "")
    books = Book.objects.all()

    if query:
        books = books.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )

    response = render(request, "bookshelf/book_list.html", {"books": books})

    # Content Security Policy header
    response["Content-Security-Policy"] = "default-src 'self'"

    return response


@csrf_protect
def form_example(request):
    """
    Demonstrates CSRF protection on forms
    """

    response = render(request, "bookshelf/form_example.html")

    # Content Security Policy header
    response["Content-Security-Policy"] = "default-src 'self'"

    return response
