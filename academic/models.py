from django.db import models
from userprofile.models import *

# Create your models here.
class StudentBatch(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    passed_year = models.DateField(blank=True,null=True)
    admission_year = models.DateField(blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.ForeignKey(AppUser,on_delete=models.CASCADE)
    user_type = models.ForeignKey(UserType,on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=255,blank=True,null=True,unique=True)
    batch = models.ForeignKey(StudentBatch,on_delete=models.CASCADE)
    photo = models.FileField(upload_to="uploads/student/",blank=True, null=True)
    linkedin_url = models.CharField(max_length=255,blank=True,null=True)
    is_alumni = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.first_name

class YearlySchedule(models.Model):
    year = models.CharField(max_length=5,blank=True,null=True)
    month_from_to = models.CharField(max_length=255,blank=True,null=True)
    year_part = models.CharField(max_length=5,blank=True,null=True)
    semester_part = models.CharField(max_length=5,blank=True,null=True)
    remarks = models.CharField(max_length=5,blank=True,null=True,default='')

    def __str__(self):
        return f"Year: {self.year}, Year Part: {self.year_part}, Semester Part: {self.semester_part}"

class StudentYearlySchedule(models.Model):
    student = models.ManyToManyField(Student)
    yearly_schedule = models.ForeignKey(YearlySchedule, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.name} - {self.yearly_schedule}"

class Publication(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    country = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    author = models.CharField(max_length=100,blank=True,null=True)
    publication  = models.ForeignKey(Publication,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SubjectYearlySchedule(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    yearly_schedule = models.ForeignKey(YearlySchedule, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject.name} - {self.yearly_schedule}"

class TheoryInternalMarks(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject = models.ForeignKey(SubjectYearlySchedule,on_delete=models.CASCADE)
    internal_assessment = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    attendance = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    class_performance = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    assignment = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    presentation = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    remarks = models.CharField(max_length=100,blank=True,null=True)

class PracticalInternalMarks(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject = models.ForeignKey(SubjectYearlySchedule,on_delete=models.CASCADE)
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



