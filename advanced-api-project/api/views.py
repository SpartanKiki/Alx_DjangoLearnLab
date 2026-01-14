from django_filters import rest_framework as filters  
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Explicitly declare filter, search, and ordering backends
    filter_backends = [filters.DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Fields for filtering using query params
    filterset_fields = ['title', 'publication_year', 'author']

    # Fields for search
    search_fields = ['title', 'author__name']

    # Fields allowed for ordering
    ordering_fields = ['title', 'publication_year', 'author__name']


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Create, Update, Delete (authenticated only)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
