from django.contrib import admin
from library_management.models import *


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name', )
    list_filter = ('is_active',)
    ordering = ('name',)
    fields = ('name', 'is_active')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_email', 'webiste', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'contact_email')
    list_filter = ('is_active',)
    ordering = ('name',)
    fields = ('name', 'address', 'webiste', 'contact_email', 'is_active')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name', )
    list_filter = ('is_active',)
    ordering = ('name',)
    fields = ('name', 'is_active')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'publisher', 'edition_number', 'publication_year', 'copies','category', 'is_active')
    search_fields = ('name', 'keyword', 'author__name', 'publisher__name')
    list_filter = ('is_active', 'publication_year')
    ordering = ('name',)
    fields = ('name', 'keyword', 'classification_number', 'author', 'publisher', 'edition_number', 'publication_year', 'copies','category', 'is_active')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(BookDetail)
class BookDetailAdmin(admin.ModelAdmin):
    list_display = ('book', 'isbn', 'accession_number')
    search_fields = ('book__name', 'isbn', 'accession_number')
    ordering = ('book',)
    fields = ('book', 'isbn', 'accession_number')


@admin.register(BorrowerType)
class BorrowerTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Borrower)
class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'registration_number', 'borrower_type')
    list_filter = ('borrower_type', 'is_active')
    search_fields = ('name', 'registration_number', 'borrower_type__name')
    ordering = ('name',)
    autocomplete_fields = ('borrower_type',)

    def get_readonly_fields(self, request, obj=None):
        if obj:  # object is being edited
            return self.readonly_fields
        return ()

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('borrower', 'book', 'number_of_copies', 'issued_date', 'returned_date', 'has_returned', 'issued_by', 'created_at', 'updated_at', 'is_active')
    list_filter = ('borrower', 'book', 'has_returned', 'is_active')
    search_fields = ('borrower__name', 'book__title')  # Adjust the fields for searching based on the related models
    date_hierarchy = 'issued_date'
    ordering = ('-issued_date',)  # Order by the most recent transaction

    # Optionally, make fields read-only or add custom validation
    readonly_fields = ('created_at', 'updated_at')