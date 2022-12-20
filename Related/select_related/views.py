from select_related.models import *
from django.db.models import F

# Create your views here.

def get_all_books():
    books = Book.objects.select_related('author').annotate(author_name=F('author__name')).values('id','name','author')
    print(books)

