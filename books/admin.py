from django.contrib import admin
from .models import Book, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Book Details", {"fields": ["title", "author"]}),
        ("Review", {"fields": ["is_favourite", "review", "date_reviewed"]}),
    ]

    readonly_fields = ("date_reviewed",)

    def book_authors(selfself, obj):
        return obj.list_author()

    book_authors.short_description = "Author(s)"

    list_display = ("title", "book_authors", "date_reviewed", "is_favourite")
    list_editable = ("is_favourite",)
    list_display_links = ("title", "date_reviewed",)
    list_filter = ("is_favourite",)
    search_fields = ("title", "author__name")

# Register your models here.
admin.site.register(Author)
