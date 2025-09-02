from django.urls import path
from library_management import views

app_name="library_management"

urlpatterns = [

    path('borrower/',views.BorrowerList.as_view(),name='borrower_list'),
    path('author/',views.AuthorList.as_view(),name='author_list'),
    path('publisher/',views.PublisherList.as_view(),name='publisher_list'),
    path('category/',views.CategoryList.as_view(),name='category_list'),

    path('borrower/create/',views.CreateBorrower.as_view(),name='create_borrower'),
    path('book/',views.BookList.as_view(),name='book_list'),
    path('available/book/',views.AvailableBookList.as_view(),name='available_book_list'),
    path('issue/book/',views.BookIssue.as_view(),name='book_issue'),
    path('borrowed/book/<int:id>/',views.BorrowedBookList.as_view(),name='borrowed_book_list'),
    path('return/book/',views.ReturnBook.as_view(),name='return_book'),
    path('transaction/',views.ActiveTransactionList.as_view(),name='transaction_list'),
    path('book/by/category/<int:id>/',views.BookByCategoryList.as_view(),name='book_bycategory_list'),


    
    # path("book/record/upload/",views.BookRecordUpload.as_view(),name="book_record_upload"),
    # path('category/',views.CategoryList.as_view(),name='category_list'),
    # path('book/by/category/<int:id>/',views.BookByCategoryList.as_view(),name='book_bycategory_list'),

    # path('available/book/',views.AvailableBookList.as_view(),name='available_book_list'),
    # path('book/issue/',views.BookIssue.as_view(),name='book_issue'),
    # path('transaction/',views.TransactionList.as_view(),name='transaction_list'),
    # path('borrowed/book/<int:id>/',views.BorrowedBookList.as_view(),name='borrowed_book_list'),
    # path('return/book/',views.ReturnBook.as_view(),name='return_book'),

    # path("borrower/record/upload/",views.BorrowerRecordUpload.as_view(),name="borrower_record_upload"),
    # path('borrower/',views.BorrowerList.as_view(),name='borrower_list'),
    # path('student/history/<int:user_id>/',views.StudentLibraryHistory.as_view(),name='student_library_history'),

    # path("book/status/by/category/",views.BookStatusByCategory.as_view(),name='book_status_by_category'),

    # path('librarian/',views.LibrarianCreate.as_view(),name='librarian_create'),


]