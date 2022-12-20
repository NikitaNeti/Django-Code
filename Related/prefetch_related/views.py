from .models import Book

# Create your views here.
def get_all_books():
    books = Book.objects.prefetch_related('publishers')

    for book in books:
        b = book.publishers.all()
        print(b)