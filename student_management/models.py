from datetime import date
from django.db import models
from userprofile.models import AppUser

# Create your models here.

class University(models.Model):
    name = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "university"
        verbose_name_plural = "university"
    
    def __str__(self):
        return self.name



class Degree(models.Model):
    name = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "degree"
        verbose_name_plural = "degree"

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "section"
        verbose_name_plural = "section"

    def __str__(self):
        return self.name

class UniversityDegree(models.Model):
    degree = models.ForeignKey(Degree,on_delete=models.CASCADE,related_name='university_degree')
    university = models.ForeignKey(University,on_delete=models.CASCADE,related_name='degree_university')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "universitydegree"
        verbose_name_plural = "universitydegree"
    
    def __str__(self):
        return f'{self.university.name} {self.degree.name}'


class AcademicBatch(models.Model):
    year = models.CharField(max_length=10,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "academic_batch"
        verbose_name_plural = "academic_batch"

    def __str__(self):
        return self.year

class AcademicSemester(models.Model):
    SEMESTER_CHOICES = [
        ('1','I/I'),
        ('2','I/II'),
        ('3','II/I'),
        ('4','II/II'),
        ('5','III/I'),
        ('6','III/II'),
        ('7','IV/I'),
        ('8','IV/II')
        ]
    number = models.CharField(choices=SEMESTER_CHOICES,max_length=25,blank=True,null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "academic_semester"
        verbose_name_plural = "academic_semesters"

    def __str__(self):
        return self.number


class DegreeBatch(models.Model):
    university_degree = models.ForeignKey(UniversityDegree,on_delete=models.CASCADE,related_name='university_degree_batch')
    academic_batch = models.ForeignKey(AcademicBatch,on_delete=models.CASCADE,related_name='university_degree_academic_batch')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "degree_batch"
        verbose_name_plural = "degree_batch"
    
    def __str__(self):
        return f'{self.university_degree.degree.name} {self.academic_batch.year}'
    


class DegreeSemester(models.Model):
    university_degree = models.ForeignKey(UniversityDegree,on_delete=models.CASCADE,related_name='university_degree_semester')
    academic_semester = models.ForeignKey(AcademicSemester,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "degree_semester"
        verbose_name_plural = "degree_semester"
    
    def __str__(self):
        return f'{self.university_degree.degree.name} {self.academic_semester.number}'




class BatchSemester(models.Model):
    degree_batch = models.ForeignKey(DegreeBatch,on_delete=models.CASCADE)
    academic_semester = models.ForeignKey(AcademicSemester,on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)

    # start_month = models.CharField(max_length=25,blank=True,null=True)
    # end_month = models.CharField(max_length=25,blank=True,null=True)
    is_running = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "batch_semester"
        verbose_name_plural = "batch_semesters"

    def __str__(self):
        return f'{self.degree_batch.university_degree.degree.name} {self.academic_semester.number}'


class Student(models.Model):
    user = models.ForeignKey(AppUser,on_delete=models.CASCADE,related_name='student_user',blank=True,null=True)
    first_name = models.CharField(max_length=255,blank=True,null=True)
    last_name = models.CharField(max_length=255,blank=True,null=True)

    registration_number =  models.CharField(unique=True,max_length=255,blank=True,null=True)
    password = models.CharField(max_length=255,blank=True,null=True)
    photo = models.FileField(upload_to="student/",blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "students"
        verbose_name_plural = "students"
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class StudentBatchSemester(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    batch_semester = models.ForeignKey(BatchSemester,on_delete=models.CASCADE)
    section = models.ForeignKey(Section,on_delete=models.CASCADE,blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "student_batch_semester"
        verbose_name_plural = "student_batch_semester"
    def __str__(self):
        return f'{self.student.first_name} {self.student.last_name} Batch: {self.batch_semester.academic_semester.number}'

# for results 
class AcademicSubject(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    code = models.CharField(max_length=25,blank=True,null=True)
    degree_semester = models.ForeignKey(DegreeSemester,on_delete=models.CASCADE)
    syllabus = models.FileField(upload_to="subject/syllabus/",blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "academic_subject"
        verbose_name_plural = "academic_subject"
    
    def __str__(self):
        return f'{self.degree_semester} || {self.name} [{self.code}]'


class Teacher(models.Model):
    user = models.ForeignKey(AppUser,on_delete=models.CASCADE,related_name='teacher_user',blank=True,null=True)
    full_name = models.CharField(max_length=25,blank=True,null=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255,blank=True,null=True)
    photo = models.FileField(upload_to="teacher/",blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "teachers"
        verbose_name_plural = "teachers"
    
    def __str__(self):
        return f'{self.full_name}'

class SubjectTeacher(models.Model):
    academic_subject = models.ForeignKey(AcademicSubject,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "subject_teacher"
        verbose_name_plural = "subject_teacher"
    
    def __str__(self):
        return f'{self.academic_subject.name} {self.teacher.full_name}'

class SubjectAttendance(models.Model):
    batch_semester = models.ForeignKey(BatchSemester,on_delete=models.CASCADE,blank=True,null=True)
    academic_subject = models.ForeignKey(AcademicSubject,on_delete=models.CASCADE,blank=True,null=True)
    day = models.DateField()
    section = models.ForeignKey(Section,on_delete=models.CASCADE,blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "subject_attendance"
        verbose_name_plural = "subject_attendance"


class StudentSubjectAttendanceRecord(models.Model):
    subject_attendance = models.ForeignKey(SubjectAttendance,on_delete=models.CASCADE)
    student_batch_semester = models.ForeignKey(StudentBatchSemester,on_delete=models.CASCADE,blank=True,null=True)
    day = models.DateField()
    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "student_subject_attendance"
        verbose_name_plural = "student_subject_attendance"
    
    # def __str__(self):
    #     return f'{self.student_batch_semester.student.first_name} {self.student_batch_semester.student.registration_number} {self.academic_subject.name} {self.day} {self.status}'


class StudentInternalExamResult(models.Model):
    academic_subject = models.ForeignKey(AcademicSubject,on_delete=models.CASCADE,blank=True,null=True)
    batch_semester = models.ForeignKey(BatchSemester,on_delete=models.CASCADE,blank=True,null=True)
    record = models.FileField(upload_to="internal/exam/",blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "student_internalexam_result"
        verbose_name_plural = "student_internalexam_result"

class StudentInternalExamResultContent(models.Model):
    student_internalexam_result = models.ForeignKey(StudentInternalExamResult,on_delete=models.CASCADE,blank=True,null=True)
    student_batch_semester = models.ForeignKey(StudentBatchSemester,on_delete=models.CASCADE,blank=True,null=True)
    marks_obtained = models.CharField(max_length=255,blank=True,null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "student_internalexam_result_content"
        verbose_name_plural = "student_internalexam_content"


    
class StudentAttendanceRecord(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    academic_subject = models.ForeignKey(AcademicSubject,on_delete=models.CASCADE)
    record = models.FileField(upload_to="subject/attendance/",blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "student_subject_attendance"
        verbose_name_plural = "student_subject_attendance"

class StudentGradeSheet(models.Model):
    student_batch_semester = models.ForeignKey(StudentBatchSemester,on_delete=models.CASCADE,blank=True,null=True)
    grade_sheet = models.FileField(upload_to="student/gradesheet/",blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "student_gradesheet"
        verbose_name_plural = "student_gradesheet"

class ExternalExamType(models.Model):
    name = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "external_exam_type"
        verbose_name_plural = "external_exam_type"
    
    def __str__(self):
        return self.name

class ExternalExamResult(models.Model):
    program = models.CharField(max_length=255,blank=True,null=True)
    examination_held_on = models.CharField(max_length=255,blank=True,null=True)
    year_semester = models.CharField(max_length=255,blank=True,null=True)
    exam_type = models.CharField(max_length=255,blank=True,null=True)
    result_published_date = models.CharField(max_length=255,blank=True,null=True)
    result_record = models.FileField(upload_to="external/result/",blank=True,null=True)
    original_result_record = models.FileField(upload_to="external/result/original/",blank=True,null=True)

class ExternalExamResultContent(models.Model):
    result_meta = models.ForeignKey(ExternalExamResult,on_delete=models.CASCADE)
    symbol_number = models.CharField(max_length=255,blank=True,null=True)
    registration_number =  models.CharField(max_length=255,blank=True,null=True)
    student_name = models.CharField(max_length=255,blank=True,null=True)
    sgpa = models.CharField(max_length=255,blank=True,null=True)
    pass_fail = models.CharField(max_length=255,blank=True,null=True)

class ExternalExamResultScore(models.Model):
    external_result_content = models.ForeignKey(ExternalExamResultContent,on_delete=models.CASCADE,blank=True,null=True)
    subject = models.CharField(max_length=255,blank=True,null=True)
    score = models.CharField(max_length=255,blank=True,null=True)

# for notices and messages 
class BatchSemesterNotice(models.Model):
    batch_semester = models.ForeignKey(BatchSemester,on_delete=models.CASCADE)
    title = models.TextField(blank=True,null=True,default="")
    messages = models.TextField(blank=True,null=True,default="")
    attachment = models.FileField(upload_to="semester/notices/",blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)
    is_active = models.BooleanField(default=True,blank=True,null=True)

























