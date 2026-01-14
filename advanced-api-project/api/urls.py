from django.urls import path
from . import views

urlpatterns = [
    # BOOK URLs
    path('books/', views.BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', views.BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),

    # AUTHOR URLs
    path('authors/', views.AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', views.AuthorRetrieveUpdateDestroyView.as_view(), name='author-detail'),
]
