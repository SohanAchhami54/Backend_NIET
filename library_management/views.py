import pandas as pd
import json
import random

from django.shortcuts import render

from library_management.models import *
from library_management.serializers import *
from student_management.models import *
from student_management.serializers import *
from userprofile.models import AppUser,UserType

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from datetime import datetime

# Create your views here.

class BorrowerList(APIView):
    def get(self,request):
        object = Borrower.objects.filter(is_active=True)
        serializer = BorrowerSerializer(object,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class BookList(APIView):
    def get(self,request):
        object = BookDetail.objects.all()

        serializer = BookDetailSerializer(object,many=True)
        df = pd.DataFrame(serializer.data)
        print(df.head())
        df['book_name'] = df['book'].map(lambda id:Book.objects.get(id=id).name)
        df['keyword'] = df['book'].map(lambda id:Book.objects.get(id=id).keyword)
        df['classification_number'] = df['book'].map(lambda id:Book.objects.get(id=id).classification_number)
        df['author'] = df['book'].map(lambda id:Book.objects.get(id=id).author.name)
        df['publisher'] = df['book'].map(lambda id:Book.objects.get(id=id).publisher.name)
        df['category'] = df['book'].map(lambda id:Book.objects.get(id=id).category.name)

        return Response(df.to_dict(orient='records'),status=status.HTTP_200_OK)

class AvailableBookList(APIView):
    def get(self,request):
        object = BookDetail.objects.all()[:10]

        serializer = BookDetailSerializer(object,many=True)
        df = pd.DataFrame(serializer.data)
        df['book_name'] = df['book'].map(lambda id:Book.objects.get(id=id).name)
        df['keyword'] = df['book'].map(lambda id:Book.objects.get(id=id).keyword)
        df['classification_number'] = df['book'].map(lambda id:Book.objects.get(id=id).classification_number)
        df['author'] = df['book'].map(lambda id:Book.objects.get(id=id).author.name)
        df['publisher'] = df['book'].map(lambda id:Book.objects.get(id=id).publisher.name)
        df['category'] = df['book'].map(lambda id:Book.objects.get(id=id).category.name)
        df = df[df['available']]

        return Response(df.to_dict(orient='records'),status=status.HTTP_200_OK)

class TransactionList(APIView):
    def get(self,request):
        object = Transaction.objects.all().order_by('-created_at')
        serializer = TransactionBaseSerializer(object,many=True)
        df = pd.DataFrame(serializer.data)
        df['book_name'] = df['book'].map(lambda id:BookDetail.objects.get(id=id).book.name)
        df['accession_number'] = df['book'].map(lambda id:BookDetail.objects.get(id=id).accession_number)
        df['issued_by'] = df['issued_by'].map(lambda id: AppUser.objects.get(id=id).email)
        return Response(df.to_dict(orient='records'),status=status.HTTP_200_OK)

class BorrowedBookList(APIView):
    def get(self,request,id):
        borrower = Borrower.objects.get(id=id)
        object = Transaction.objects.filter(borrower=borrower,has_returned=False).order_by('-created_at')
        serializer = TransactionBaseSerializer(object,many=True)
        df = pd.DataFrame(serializer.data)
        df['book_name'] = df['book'].map(lambda id:BookDetail.objects.get(id=id).book.name)
        df['accession_number'] = df['book'].map(lambda id:BookDetail.objects.get(id=id).accession_number)
        df['issued_by'] = df['issued_by'].map(lambda id: AppUser.objects.get(id=id).email)
        return Response(df.to_dict(orient='records'),status=status.HTTP_200_OK)


class BookRecordUpload(APIView):
    parser_classes = [MultiPartParser,FormParser]
    def post(self,request,*args,**kwargs):
        print(request.data)
        serializer = BookRecordUploadSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data['file']
            # try:
            df = pd.read_excel(file,header=0)      
            records = df.to_dict('records')

            for record in records:
                author,_ = Author.objects.get_or_create(name=record['AuthorName'])
                publisher,_ = Publisher.objects.get_or_create(name=record['PublisherName'])
                category,_ = Category.objects.get_or_create(name=record['Category'])
                book = Book.objects.filter(classification_number=record['ClassificationNumber'])

                if not book:
                    book = Book.objects.create(
                        name = record['BookName'],
                        keyword = record['Keywords'],
                        classification_number = record['ClassificationNumber'],
                        author = author,
                        publisher = publisher,
                        category = category
                    )
                    book_detail = BookDetail.objects.create(
                        book = book,
                        accession_number = record['AccessionNumber']
                    )
                else:
                    book_detail = BookDetail.objects.filter(
                        book = book[0],
                        accession_number = record['AccessionNumber'])
                    if not book_detail:
                        book_detail = BookDetail.objects.create(
                            book = book[0],
                            accession_number = record['AccessionNumber']
                        )
            return Response({'status':'success'},status=status.HTTP_201_CREATED)
        return Response({'status':'Error'},status=status.HTTP_400_BAD_REQUEST)

class BookIssue(APIView):
    def post(self,request):
        data = request.data
        borrower_id = data['borrower']
        books = json.loads(data['books'])

        try:
            borrower = Borrower.objects.get(id=borrower_id)
        except Exception as e:
            return Response({"message":"borrower doesnot exist"},status=status.HTTP_400_BAD_REQUEST)
        try:
            for book in books:
                transaction = Transaction()
                transaction.borrower = borrower
                bobj = BookDetail.objects.get(id=book['id'])
                transaction.book = bobj
                transaction.issued_by = request.user
                transaction.save()
                bobj.is_active = False
                bobj.save()
            return Response({'status':'success'},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message':repr(e)},status=status.HTTP_400_BAD_REQUEST)

class ReturnBook(APIView):
    def post(self,request):

        record = request.data
        try:
            transaction = Transaction.objects.get(id=record['record_id'])
            transaction.has_returned = True
            transaction.returned_date = datetime.now()
            transaction.save()
            # book_detail = BookDetail.objects.get(id=transaction.book.id)
            # book_detail.is_active = True
            # book_detail.save()
            return Response({'status':'success'},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'status':repr(e)},status=status.HTTP_400_BAD_REQUEST)

class BorrowerList(APIView):
    def get(self,request):
        borrowers = Borrower.objects.filter(is_active=True)
        serializer = BorrowerBaseSerializer(borrowers,many=True)
        df = pd.DataFrame(serializer.data)
        df['borrower_type'] = df['borrower_type'].map(lambda id:BorrowerType.objects.get(id=id).name)
        return Response(df.to_dict(orient='records'),status=status.HTTP_200_OK)


class BorrowerRecordUpload(APIView):
    parser_classes = [MultiPartParser,FormParser]
    def post(self,request,*args,**kwargs):
        students = Student.objects.filter(is_active=True)
        for student in students:
            borrower = Borrower.objects.filter(registration_number=student.registration_number)
            if not borrower:
                borrower = Borrower.objects.create(
                    borrower_type = BorrowerType.objects.get(name='student'),
                    name = f'{student.first_name} {student.last_name}',
                    registration_number=student.registration_number
                    )

        serializer = BookRecordUploadSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data['file']
            df = pd.read_excel(file,header=0)      
            records = df.to_dict('records')
            try:
                for record in records:
                    borrower = Borrower.objects.filter(registration_number=record['RegistrationNumber'])
                    if not borrower:
                        borrower = Borrower.objects.create(
                            borrower_type = BorrowerType.objects.get(name=record['Type']),
                            name = record['Name'],
                            phone = record['Phone'],
                            email = record['Email'],
                            registration_number=record['RegistrationNumber']
                            )
                return Response({'status':'success'},status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'Message':'Error Adding records'},status=status.HTTP_400_BAD_REQUEST)

class StudentLibraryHistory(APIView):
        def get(self,request,user_id):
            user = AppUser.objects.get(id=user_id)
            student = Student.objects.get(user=user)
            borrower = Borrower.objects.get(registration_number=student.registration_number)
            object = Transaction.objects.filter(borrower=borrower).order_by('-created_at')
            serializer = TransactionBaseSerializer(object,many=True)
            df = pd.DataFrame(serializer.data)
            df['book_name'] = df['book'].map(lambda id:BookDetail.objects.get(id=id).book.name)
            df['accession_number'] = df['book'].map(lambda id:BookDetail.objects.get(id=id).accession_number)
            df['issued_by'] = df['issued_by'].map(lambda id: AppUser.objects.get(id=id).email)
            return Response(df.to_dict(orient='records'),status=status.HTTP_200_OK)

class LibrarianCreate(APIView):
    def post(self,request):
        full_name = request.data['full_name']
        email = request.data['email']
        user_type = UserType.objects.get(name='Librarian')
        app_user = AppUser.objects.filter(email=email)
        if app_user:
            return Response({'message':'App user with email already exists'},status=status.HTTP_400_BAD_REQUEST)

        generated_password = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        user = AppUser.objects.create_user(email=email,password=generated_password)
        user.usertype = user_type
        user.save()
        librarian = Librarian.objects.create(
            user = user,
            full_name = full_name,
            password = generated_password,
            )
        return Response({'status':'success'},status=status.HTTP_201_CREATED)


        
        







