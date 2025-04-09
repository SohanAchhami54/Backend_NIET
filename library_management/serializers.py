from rest_framework import serializers
from library_management.models import *
from userprofile.serializers import AppUserPublicSerializer

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'created_at', 'updated_at', 'is_active']

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'address', 'webiste', 'contact_email', 'created_at', 'updated_at', 'is_active']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at', 'updated_at', 'is_active']


class BookBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  # Nested serializer to include author details
    publisher = PublisherSerializer()  # Nested serializer to include publisher details
    category = CategorySerializer()

    class Meta:
        model = Book
        fields = [
            'id', 'name', 'keyword', 'classification_number', 'author', 'publisher','category', 
            'edition_number', 'publication_year', 'copies', 'created_at', 'updated_at', 'is_active'
        ]

class BookDetailSerializer(serializers.ModelSerializer):
    # book = BookSerializer()  
    # book = BookBaseSerializer()
    available = serializers.SerializerMethodField()
    class Meta:
        model = BookDetail
        fields = ['id', 'book', 'isbn', 'accession_number','available']
    
    def get_available(self, obj):
        # Check if there are any transactions where has_returned=False for this book
        is_issued = Transaction.objects.filter(book=obj, has_returned=False).exists()
        return not is_issued

class BookDetailSearchSerializer(serializers.ModelSerializer):
    book = BookSerializer()  
    available = serializers.SerializerMethodField()

    class Meta:
        model = BookDetail
        fields = ['id', 'book', 'isbn', 'accession_number','available']
    
    def get_available(self, obj):
        # Check if there are any transactions where has_returned=False for this book
        is_issued = Transaction.objects.filter(book=obj, has_returned=False).exists()
        return not is_issued



class BorrowerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowerType
        fields = '__all__'

class BorrowerBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = '__all__'

class BorrowerSerializer(serializers.ModelSerializer):
    borrower_type = BorrowerTypeSerializer()
    class Meta:
        model = Borrower
        fields = ['id','borrower_type','name','email','phone','registration_number',]

class TransactionBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    borrower = BorrowerSerializer()
    book = BookDetailSerializer()
    issued_by = AppUserPublicSerializer()
    class Meta:
        model = Transaction
        fields = ['id','borrower','book','issued_date','returned_date','has_returned','issued_by']


class BookRecordUploadSerializer(serializers.Serializer):
    file = serializers.FileField()


class BorrowerRecordUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Librarian
        fields = '__all__'

