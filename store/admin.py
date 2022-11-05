from django.contrib import admin

from store.models import Author, Publisher, Book


@admin.register(Author)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", )

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publisher", "price", "quantity", )
    search_fields = ("title", "author", "publisher", )
    list_filter = ("price", "quantity", )
    autocomplete_fields = ("author", "publisher", )
