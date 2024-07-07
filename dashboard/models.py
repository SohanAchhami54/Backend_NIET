from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from userprofile.models import *

# Create your models here.
class Schedule(models.Model):
    year_part = models.CharField(max_length=5,blank=True,null=True)
    semester_part = models.CharField(max_length=5,blank=True,null=True)
    remarks = models.CharField(max_length=5,blank=True,null=True,default='')

    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)
    is_active = models.BooleanField(default=True,blank=True,null=True)

    def __str__(self):
        return f"Year Part: {self.year_part}, Semester Part: {self.semester_part}"
    
class YearlyScheduler(models.Model):
    year = models.CharField(max_length=5,blank=True,null=True)
    month_from_to = models.CharField(max_length=255,blank=True,null=True)
    schedule = models.ForeignKey(Schedule,on_delete=models.CASCADE)
    remarks = models.CharField(max_length=5,blank=True,null=True,default='')

    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)
    is_active = models.BooleanField(default=True,blank=True,null=True)

    def __str__(self):
        return f"Year: {self.year}"

# class YearlySchedule(models.Model):
#     year = models.CharField(max_length=5,blank=True,null=True)
#     month_from_to = models.CharField(max_length=255,blank=True,null=True)
#     schedule = models.ForeignKey(Schedule,on_delete=models.CASCADE,blank=True,null=True)
#     remarks = models.CharField(max_length=5,blank=True,null=True,default='')

#     created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
#     updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)
#     is_active = models.BooleanField(default=True,blank=True,null=True)

#     def __str__(self):
#         return f"Year: {self.year}"
    

class Student(models.Model):
    user = models.ForeignKey(AppUser,related_name='users',on_delete=models.CASCADE)
    user_type = models.ForeignKey(UserType,on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=255,blank=True,null=True,unique=True)
    photo = models.FileField(upload_to="uploads/student/",blank=True, null=True)
    linkedin_url = models.CharField(max_length=255,blank=True,null=True)
    is_alumni = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.first_name

class StudentYearlyScheduler(models.Model):
    student = models.ForeignKey(Student,related_name='yearlyschedules_student',on_delete=models.CASCADE)
    yearly_schedule = models.ForeignKey(YearlyScheduler,related_name='yearlyschedules_schedule', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)
    is_active = models.BooleanField(default=True,blank=True,null=True)

    def __str__(self):
        return f"{self.student.user.first_name} - {self.yearly_schedule}"

# class StudentYearlySchedule(models.Model):
#     student = models.ManyToManyField(Student,related_name='studentyearlyschedules')
#     yearly_schedule = models.ForeignKey(YearlySchedule, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.student.name} - {self.yearly_schedule}"

class Batch(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    passed_year = models.DateField(blank=True,null=True)
    admission_year = models.DateField(blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class StudentBatch(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,blank=True,null=True, default='')
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE,blank=True,null=True, default='')

    def __str__(self):
        return f"{self.student.name} - {self.batch.passed_year}"


# class Publication(models.Model):
#     name = models.CharField(max_length=100,blank=True,null=True)
#     country = models.CharField(max_length=100,blank=True,null=True)
#     def __str__(self):
#         return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    code = models.CharField(max_length=100,blank=True,null=True)
    syllabus = CKEditor5Field('syllabus', config_name='extends',blank=True,null=True)
    references = CKEditor5Field('references', config_name='extends',blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class SubjectSchedule(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject.name} - {self.schedule}"

class TheoryInternalMarks(models.Model):
    student_yearly_scheduler = models.ForeignKey(StudentYearlyScheduler,on_delete=models.CASCADE,default='')
    subject = models.ForeignKey(SubjectSchedule,on_delete=models.CASCADE)
    internal_assessment = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    attendance = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    class_performance = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    assignment = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    presentation = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    remarks = models.CharField(max_length=100,blank=True,null=True)

class PracticalInternalMarks(models.Model):
    student_yearly_scheduler = models.ForeignKey(StudentYearlyScheduler,on_delete=models.CASCADE,default='')
    subject = models.ForeignKey(SubjectSchedule,on_delete=models.CASCADE)
    labexam_viva = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    attendance = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    lab_report = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)





    

# class Project(models.Model):
#     title = models.CharField(max_length=255,blank=True,null=True)
#     abstract = CKEditor5Field('abstract', config_name='extends',blank=True,null=True)
#     batch = models.ForeignKey(StudentBatch,on_delete=models.CASCADE)
#     category = models.ForeignKey(ProjectCategory,on_delete=models.CASCADE)
#     supervisor_name = models.CharField(max_length=255,blank=True,null=True)
#     students = models.ManyToManyField(Student)

#     def __str__(self):
#         return self.title



