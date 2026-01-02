from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library


def list_books(request):
    books = Book.objects.all()
    output = []
    for book in books:
        output.append(f"{book.title} by {book.author.name}")
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render

class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class UserLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

