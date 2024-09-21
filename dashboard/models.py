
from django.db import models
from userprofile.models import AppUser

# Create your models here.

class Batch(models.Model):
    number = models.CharField(max_length=25,blank=True,null=True)
    year = models.CharField(max_length=10,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "batch"
        verbose_name_plural = "batches"

    def __str__(self):
        return f"{self.year}-{self.number}"

class Semester(models.Model):
    SEMESTER_CHOICES = [
        ('I/I','1'),
        ('I/II','2'),
        ('II/I','3'),
        ('II/II','4'),
        ('III/I','5'),
        ('III/II','6'),
        ('IV/I','7'),
        ('IV/II','8')
        ]
    batch = models.ForeignKey(Batch,on_delete=models.CASCADE)
    number = models.CharField(choices=SEMESTER_CHOICES,max_length=25,blank=True,null=True)
    start_month = models.CharField(max_length=25,blank=True,null=True)
    end_month = models.CharField(max_length=25,blank=True,null=True)
    is_current = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "semester"
        verbose_name_plural = "semesters"

    def __str__(self):
        return f"{self.batch.year}-{self.number}"

class Subject(models.Model):
    name = models.CharField(max_length=25,blank=True,null=True)
    code = models.CharField(max_length=25,blank=True,null=True)
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "subjects"
        verbose_name_plural = "subjects"

    def __str__(self):
        return f"{self.name}"

class Student(models.Model):
    user = models.ForeignKey(AppUser,on_delete=models.CASCADE,blank=True,null=True)
    full_name = models.CharField(max_length=255,blank=True,null=True)
    symbol_number = models.CharField(max_length=255,blank=True,null=True)
    registration_number =  models.CharField(max_length=255,blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "students"
        verbose_name_plural = "students"

    def __str__(self):
        return f"{self.full_name}"

class StudentInSemester(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "studentsinsemester"
        verbose_name_plural = "studentsinsemester"

    def __str__(self):
        return f"{self.student.full_name}-{self.semester.number}"

class ExamType(models.Model):
    name = models.CharField(max_length=25,blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "examtype"
        verbose_name_plural = "examtypes"

    def __str__(self):
        return f"{self.name}"

class SubjectInternalExam(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    exam_type = models.ForeignKey(ExamType,on_delete=models.CASCADE)
    full_marks = models.DecimalField(max_digits=10,decimal_places=2,default=100)
    pass_marks = models.DecimalField(max_digits=10,decimal_places=2,default=32)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "subjectinternalexam"
        verbose_name_plural = "subjectinternalexam"

    def __str__(self):
        return f"{self.subject.name}"

class StudentInternalExamResult(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject_internalexam = models.ForeignKey(SubjectInternalExam,on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(max_digits=10,decimal_places=2,default=32)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "subjectinternalexam"
        verbose_name_plural = "subjectinternalexam"

    def __str__(self):
        return f"{self.student.full_name}"

class StudentSubjectAttendance(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    day = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "studentssubjectattendance"
        verbose_name_plural = "studentssubjectattendance"

    def __str__(self):
        return f"{self.student.full_name}"

class Teacher(models.Model):
    user = models.ForeignKey(AppUser,on_delete=models.CASCADE,blank=True,null=True)
    full_name = models.CharField(max_length=25,blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "teachers"
        verbose_name_plural = "teachers"

    def __str__(self):
        return f"{self.full_name}"

class SubjectTeacher(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "subjectteacher"
        verbose_name_plural = "subjectteacher"

    def __str__(self):
        return f"{self.teacher.full_name}"































