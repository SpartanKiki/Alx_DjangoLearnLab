from django_filters import rest_framework as filters  # This gives us filters.DjangoFilterBackend, filters.OrderingFilter
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [
        filters.DjangoFilterBackend,  # For field-based filtering
        filters.SearchFilter,         # For search functionality
        filters.OrderingFilter        # For ordering functionality
    ]

    # Fields allowed to filter by
    filterset_fields = ['title', 'author', 'publication_year']

    # Fields allowed to search
    search_fields = ['title', 'author__name']

    # Fields allowed to order by
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
