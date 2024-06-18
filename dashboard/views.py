import json
import pandas as pd
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils.timezone import now
import openpyxl
from openpyxl.utils.datetime import from_excel

# from general.models import UserType, AppUser, StudentBatch, Student
from django.contrib.auth.hashers import make_password
import random
import string

from dashboard.models import *
from general.models import *
from dashboard.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser





from celery import shared_task

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.
# Create your views here.
def admin_dashboard(request):
    students = Student.objects.filter(is_active=True,is_alumni=True)
    student_count =  Student.objects.filter(is_active=True,is_alumni=True).count()
    visitingfaculty_count =  Faculty.objects.filter(
        faculty_type__type_name='visiting', 
        faculty_type__is_active=True
    ).count()
    fullfaculty_count =  Faculty.objects.filter(
        faculty_type__type_name='full time', 
        faculty_type__is_active=True
    ).count()
    context_dict = {
        'students':students,'student_count':student_count,
        'visitingfaculty_count':visitingfaculty_count,
        'fullfaculty_count':fullfaculty_count,
        }
    return render(request,'dashboard/index.html',context_dict)

@shared_task
def send_registration_email(user, password):
    subject = 'Welcome to Our College!'
    context = {
        'user': user,
        'password': password,
        'year': datetime.now().year
    }
    html_message = render_to_string('email_template.html', context)
    plain_message = strip_tags(html_message)
    from_email = 'infymee@gmail.com'
    to = user.email
    
    send_mail(subject, plain_message, from_email, [to], html_message=html_message)

def dashboard(request):
    return render(request, "index.html")




def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def bulk_upload_students(request):
    if request.method == "POST":
        try:
            
            excel_file = request.FILES["file"]
            
            wb = openpyxl.load_workbook(excel_file)
            sheet = wb.active
            
            user_type = UserType.objects.get(name="Student")
            
            for row in sheet.iter_rows(min_row=2, values_only=True):
                print(row)
                first_name, middle_name, last_name, email, batch_name, admission_year, passed_year, registration_number = row
                if not email:
                    continue  # Skip rows with no email
                
                # Create AppUser
                password = generate_random_password()
                
                user = AppUser.objects.filter(email=email)
                if user:
                    continue
                
                user = AppUser.objects.create(
                    first_name=first_name,
                    middle_name=middle_name,
                    last_name=last_name,
                    email=email,
                    is_active=True,
                    is_staff=False,
                    date_joined=now(),
                    password=make_password(password)
                )
                print(first_name,password)

                admission_year = str(admission_year).split(".")[0]
                passed_year = str(passed_year).split(".")[0]

                admission_year = datetime.strptime(admission_year,"%Y")
                passed_year  = datetime.strptime(passed_year,"%Y")

                
                print(admission_year,passed_year)
                
                # Get or create StudentBatch

                # batch, created = StudentBatch.objects.get_or_create(
                #     name=batch_name,
                #     admission_year=admission_year,
                #     passed_year=passed_year,
                #     defaults={'is_active': True}
                # )

                # Create Student
                student = Student.objects.create(
                    user=user,
                    user_type=user_type,
                    # batch=batch,
                    registration_number=registration_number
                    # is_alumni = is_alumni
                )
                try:
                    send_registration_email(user,password)
                except Exception as e:
                    print(e)
            
            return JsonResponse({'message': 'Students have been uploaded successfully.'}, status=200)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)
    return render(request, "dashboard/index.html")


def bulk_upload_faculty(request):
    if request.method == "POST":
        try:
            
            excel_file = request.FILES["file"]
            
            wb = openpyxl.load_workbook(excel_file)
            sheet = wb.active
            
            user_type = UserType.objects.get(name="Teacher")
            
            for row in sheet.iter_rows(min_row=2, values_only=True):
                first_name, middle_name, last_name, email, education,designation,post_name,faculty_type = row
                
                if not (first_name and last_name and email and education and designation and post_name and faculty_type):
                    continue  
                if not email:
                    continue  # Skip rows with no email
                
                # Create AppUser
                password = generate_random_password()
                
                user = AppUser.objects.filter(email=email)
                if user:
                    continue
                
                user = AppUser.objects.create(
                    first_name=first_name,
                    middle_name=middle_name,
                    last_name=last_name,
                    email=email,
                    is_active=True,
                    is_staff=False,
                    date_joined=now(),
                    password=make_password(password)
                )
                
                ftype,created = FacultyType.objects.get_or_create(type_name=faculty_type)

                # Create Faculty
                Faculty.objects.create(
                    user=user,
                    user_type=user_type,
                    education = education,
                    designation = designation,
                    post_name = post_name,
                    faculty_type = ftype
                )

            
            return JsonResponse({'message': 'Faculty have been uploaded successfully.'}, status=200)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)
    return render(request, "index.html")

# prakash Z9Iqwo6c




# API view defined here

class YearlyScheduleList(APIView):
    """
    List all yearlyschedule, or create a new yearlyschedule.
    """
    def get(self, request, format=None):
        items = YearlySchedule.objects.filter(is_active=True)
        serializer = YearlyScheduleSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = YearlyScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentYearlyScheduleUpload(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file = request.data.get('file')
        yearly_schedule_id = request.data.get('yearly_schedule')

        if not file or not yearly_schedule_id:
            return Response(
                {"error": "File and yearly schedule are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            yearly_schedule = YearlySchedule.objects.get(id=yearly_schedule_id)
        except YearlySchedule.DoesNotExist:
            return Response(
                {"error": "Yearly schedule not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            df = pd.read_excel(file)
            # students = []
            user_type = UserType.objects.get(name="Student")

            for _, row in df.iterrows():
                if not row['email']:
                    continue  
                
                # Create AppUser
                password = generate_random_password()
                
                user = AppUser.objects.filter(email=row['email'])
                if user:
                    continue
                
                user = AppUser.objects.create(
                    first_name=row['first_name'],
                    middle_name=row['middle_name'],
                    last_name=row['last_name'],
                    email=row['email'],
                    is_active=True,
                    is_staff=False,
                    date_joined=now(),
                    password=make_password(password)
                )
                student, created = Student.objects.get_or_create(
                    user=user,
                    user_type=user_type,
                    # batch=batch,
                    registration_number=row['registration_number']
                    # is_alumni = is_alumni
                )
                # students.append(student)
                student_yearly_scheduler = StudentYearlyScheduler.objects.create(
                    yearly_schedule=yearly_schedule,
                    student=student
                    )
                student_yearly_scheduler.save()

            return Response(
                {"message": "Students uploaded and linked to the yearly schedule successfully"},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        

class StudentYearlyScheduleList(APIView):
    def get(self, request,schedule_id):
        yearly_schedule_id = schedule_id
        try:
            yearly_schedule = StudentYearlyScheduler.objects.filter(yearly_schedule__id=yearly_schedule_id,is_active=True)
            serializer = StudentYearlySchedulerSerializer(yearly_schedule,many=True)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class StudentYearlyScheduleUpdate(APIView):
    def post(self,request):
        yearly_schedule_id = request.data.get('yearly_schedule')
        student_ids = request.data.get('selected_ids').split(',')
        yearly_schedule = YearlySchedule.objects.get(id=yearly_schedule_id)
        for id in student_ids:
            student = Student.objects.get(id=id)
            student_yearly_schedule = StudentYearlyScheduler.objects.get(yearly_schedule=yearly_schedule,student=student)
            student_yearly_schedule.is_active = False
            student_yearly_schedule.save()
        return Response(
            {"message": "Students yearly schedule updated successfully"},
            status=status.HTTP_202_ACCEPTED
        )




