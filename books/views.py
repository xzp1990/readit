from django.db.models import Count
from django.shortcuts import render
from django.views.generic import View, DetailView
from .models import Author, Book

# Create your views here.
#Functional view
def list_books(request):
    """
    List the books that have reviews
    """

    books = Book.objects.exclude(date_reviewed__isnull=True).prefetch_related('author')

    context = {
        'books':books,
    }

    return render(request, "list.html", context)

#Class base view
class Authorlist(View):
    def get(self, request):

        authors = Author.objects.annotate(
            published_books=Count('books')
        ).filter(
            published_books__gt=0
        )

        context = {
            'authors': authors,
        }

        return render(request, "authors.html", context)

#Class-Based Generic view
class BookDetail(DetailView):
    model = Book
    template_name = "book.html"

class AuthorDetail(DetailView):
    model = Author
    template_name = "author.html"