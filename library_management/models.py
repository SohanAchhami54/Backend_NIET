from django.db import models
from userprofile.models import AppUser
# from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    # last_name = models.CharField(max_length=255,blank=True,null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "author"
        verbose_name_plural = "authors"

    def __str__(self):
        return f"{self.name} "

class Publisher(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    webiste = models.CharField(max_length=255,blank=True,null=True)
    contact_email = models.CharField(max_length=255,blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "publisher"
        verbose_name_plural = "publishers"

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    keyword = models.CharField(max_length=255,blank=True,null=True)
    classification_number = models.CharField(max_length=255,blank=True,null=True)
    # classification_number = models.DecimalField(unique=True, max_digits=20,decimal_places=5,blank=True,null=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    edition_number = models.CharField(max_length=255,blank=True,null=True)
    publication_year = models.CharField(max_length=255,blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    copies = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "book"
        verbose_name_plural = "books"

    def __str__(self):
        return f"{self.name}"

class BookDetail(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True, help_text="13-character ISBN",blank=True,null=True)
    accession_number = models.CharField(unique=True,max_length=255,blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "book_detail"
        verbose_name_plural = "book_details"

    def __str__(self):
        return f"{self.book.name} - {self.accession_number}"

class BorrowerType(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    class Meta:
        verbose_name = "borrower_type"
        verbose_name_plural = "borrower_types"

    def __str__(self):
        return f"{self.name}"


class Borrower(models.Model):
    borrower_type = models.ForeignKey(BorrowerType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    registration_number = models.CharField(unique=True, max_length=255, blank=True, null=True)
    # library_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    photo = models.FileField(upload_to='uploads/photo/',blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(unique=True, max_length=20, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "borrower"
        verbose_name_plural = "borrowers"

    def __str__(self):
        return f"{self.name}"

class Transaction(models.Model):
    borrower = models.ForeignKey(Borrower,on_delete=models.CASCADE)
    book = models.ForeignKey(BookDetail,on_delete=models.CASCADE)
    number_of_copies = models.IntegerField(default=1) 
    issued_date = models.DateTimeField(auto_now_add=True)
    returned_date = models.DateTimeField(blank=True,null=True)
    has_returned = models.BooleanField(default=False)
    issued_by = models.ForeignKey(AppUser,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "transaction"
        verbose_name_plural = "transactions"
    













    






