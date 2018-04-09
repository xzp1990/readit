from django.db.models import Count
from django.shortcuts import get_object_or_404, render
from django.views.generic import View, DetailView
from .models import Author, Book
from .forms import ReviewForm

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

def review_books(request):
    """
    List all the books that we want to review.
    :return:
    """
    books = Book.objects.filter(date_reviewed__isnull=True).prefetch_related('author')

    context = {
        'books': books,
    }

    return render(request, "list-to-review.html", context)

def review_book(request, pk):
    """
    Review an indivial book
    :param pk:
    :return:
    """
    book = get_object_or_404(Book, pk=pk)
    form = ReviewForm

    context = {
        'book': book,
        'form': form,
    }
    return render(request, "review-book.html", context)
