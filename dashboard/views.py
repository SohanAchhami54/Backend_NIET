import json
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils.timezone import now
import openpyxl
from openpyxl.utils.datetime import from_excel

# from general.models import UserType, AppUser, StudentBatch, Student
from general.models import *
from academic.models import *
from django.contrib.auth.hashers import make_password
import random
import string

from django.shortcuts import render
from general.models import *
from academic.models import *

from celery import shared_task

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.


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
                batch, created = StudentBatch.objects.get_or_create(
                    name=batch_name,
                    admission_year=admission_year,
                    passed_year=passed_year,
                    defaults={'is_active': True}
                )

                # Create Student
                student = Student.objects.create(
                    user=user,
                    user_type=user_type,
                    batch=batch,
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
    return render(request, "dashboard/index.html")

# prakash Z9Iqwo6c

