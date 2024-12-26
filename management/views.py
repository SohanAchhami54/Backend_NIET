import random
import pandas as pd
import json

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from userprofile.models import AppUser,UserType
from management.models import Student,Teacher,Semester,Subject,SubjectTeacher,BatchSemester,StudentInSemester,StudentSubjectAttendance,ExamType,SubjectInternalExam,StudentInternalExamResult,ExamSession,Notice
from management.serializers import SemesterSerializer,SubjectSerializer,TeacherSerializer,SubjectTeacherDetailSerializer,BatchSemesterDetailSerializer,StudentInSemesterSerializer,ExamTypeSerializer,ExamSessionSerializer,StudentSubjectAttendanceSerializer,StudentInternalExamResultSerializer,DetailSubjectTeacherSerializer,NoticeSerializer,StudentSubjectAttendanceDetailSerializer,StudentRecordUploadSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from rest_framework.parsers import MultiPartParser, FormParser




# Create your views here.
def handle_login(request):
    if request.method == 'POST':
        print('i am here')
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email=email,password=password)
        print("at login")
        if user is not None:
            login(request,user)
            if user.is_staff or user.is_superuser:
                return redirect("/dashboard/admin/")
            elif user.usertype.name=='Student':
                return redirect("/dashboard/student/")
            elif user.usertype.name=='Teacher':
                return redirect("/dashboard/teacher/")
            else:
                logout(request)
                return redirect("/")

    return render(request,'login.html')

def handle_logout(request):
    logout(request)
    return redirect('/dashboard/login/')

@login_required(login_url='/dashboard/login/')
def handle_admin(request):
    print("hello")
    print(request.user.is_superuser,request.user.is_staff)
    if request.user.is_superuser or request.user.is_staff:
        return render(request,'admin.html')
    else:
        logout(request)
        return redirect("/")

@login_required(login_url='/dashboard/login/')
def handle_student(request):
    if request.user.usertype.name=='Student':
        user = AppUser.objects.get(id=request.user.id)
        student = Student.objects.get(user=user)
        return render(request,'student.html',{'student':student})
    else:
        logout(request)
        return redirect("/")

@login_required(login_url='/dashboard/login/')
def handle_teacher(request):
    print(request.user.usertype)
    if request.user.usertype.name=='Teacher':
        user = AppUser.objects.get(id=request.user.id)
        teacher = Teacher.objects.get(user=user)
        return render(request,'teacher.html',{'teacher':teacher})
    else:
        logout(request)
        return redirect("/")  

# upload student record 

class StudentRecordUpload(APIView):
    parser_classes = [MultiPartParser,FormParser]
    def post(self,request,*args,**kwargs):
        serializer = StudentRecordUploadSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data['file']
            df = pd.read_excel(file,header=0)
            records = df.to_dict('records')
            for record in records:
                try:
                    first_name = record.get('First Name ', '').strip()
                    last_name = record.get('Last Name ', '').strip()
                    email_address = record.get('Email Address ', '').strip()
                    registration_num = record.get('Registration No.', '').strip()
                except Exception as e:
                    continue

                student_obj = Student.objects.filter(registration_number=registration_num)
                if not email_address and first_name and last_name and registration_num:
                    continue
                if not student_obj:
                    user_type = UserType.objects.get(name='Student')
                    generated_password = ''.join([str(random.randint(0, 9)) for _ in range(4)])
                    user = AppUser.objects.create_user(email=email_address,password=generated_password)
                    user.usertype = user_type
                    user.save()
                    student = Student.objects.create(
                        user = user,
                        first_name = first_name,
                        last_name = last_name,
                        registration_number = registration_num,
                        password = generated_password,
                        )
            return Response({'status':'success'},status=status.HTTP_201_CREATED)
        else:
            return Response({'status':'Error'},status=status.HTTP_400_BAD_REQUEST)     

# register a student 
class RegisterStudent(APIView):
    def post(self,request):
        print(request.data)
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        # symbol_number = request.data['symbol_number']
        registration_number = request.data['registration_number']
        batch_semester_id = request.data['batchsemester']
        photo = request.FILES.get('file')
        # print(photo)

        user_type = UserType.objects.get(name='Student')
        generated_password = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        # register a student 
        # try:
        user = AppUser.objects.create_user(email=email,password=generated_password)
        user.usertype = user_type
        user.save()
        student = Student.objects.create(
            user = user,
            first_name = first_name,
            last_name = last_name,
            registration_number = registration_number,
            password = generated_password,
            photo = photo
        )
        batch_semester = BatchSemester.objects.get(id=batch_semester_id)
        student_in_semester = StudentInSemester.objects.create(student=student,semester=batch_semester)
        student_in_semester.save()

        # except Exception as e:
        #     return Response({'message':"error registering student"},status=status.HTTP_400_BAD_REQUEST)

        return Response({'message':"student successfully registered"},status=status.HTTP_201_CREATED)

# register a teacher 
class RegisterTeacher(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password'].strip()
        photo = request.FILES.get('file')
        full_name = request.data['full_name']
        user_type = UserType.objects.get(name='Teacher')
        generated_password = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        # register a student 
        try:
            user = AppUser.objects.create_user(email=email,password=generated_password)
            user.usertype = user_type
            user.save()
            teacher = Teacher.objects.create(
                user = user,
                full_name = full_name,
                password = generated_password,
                photo = photo
            )
        except Exception as e:
            return Response({'message':"error registering teacher"},status=status.HTTP_400_BAD_REQUEST)

        return Response({'message':"teacher successfully registered"},status=status.HTTP_201_CREATED)

# password reset 
class PasswordReset(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password'].strip()
        # register a student 
        try:
            user = AppUser.objects.get(email=email)
            user.set_password(password)
            user.save()
            student = Student.objects.filter(user=user)
            teacher = Teacher.objects.filter(user=user)
            if student:
                student = Student.objects.get(user=user)
                student.password = password
                student.save()
            if teacher:
                teacher = Teacher.objects.get(user=user)
                teacher.password = password
                teacher.save()

        except Exception as e:
            return Response({'message':"error registering teacher"},status=status.HTTP_400_BAD_REQUEST)

        return Response({'message':"teacher successfully registered"},status=status.HTTP_201_CREATED)
    

# semester fetch 
class SemesterList(APIView):
    def get(self,request):
        semesters = Semester.objects.filter(is_active=True)
        serializer = SemesterSerializer(semesters,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class TeacherList(APIView):
    def get(self,request):
        teachers = Teacher.objects.filter(is_active=True)
        serializer = TeacherSerializer(teachers,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class SubjectList(APIView):
    def get(self,request,sem_id):
        try:
            semester = Semester.objects.get(id=sem_id, is_active=True)
        except Semester.DoesNotExist:
            return Response({'message':'semester does not exist'},status=status.HTTP_400_BAD_REQUEST)
        try:
            subjects = Subject.objects.filter(semester=semester)
        except Subject.DoesNotExist:
            return Response({'message':'subject does not exist'},status=status.HTTP_400_BAD_REQUEST)
        serializer = SubjectSerializer(subjects,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class AssignSubjectTeacher(APIView):
    def post(self,request):
        subject_id = request.data['selectedSubject']
        teacher_id = request.data['selectedTeacher']

        subject = Subject.objects.get(id=subject_id)
        teacher = Teacher.objects.get(id=teacher_id)
        sub = SubjectTeacher.objects.filter(subject=subject)
        if sub:
            return Response({'message':"Error assigning subject teacher "},status=status.HTTP_400_BAD_REQUEST)
        obj = SubjectTeacher.objects.filter(subject=subject,teacher=teacher)
        if obj:
            return Response({'message':"Error assigning subject teacher "},status=status.HTTP_400_BAD_REQUEST)

        subject_teacher = SubjectTeacher.objects.create(subject=subject,teacher=teacher)
        if subject_teacher:
            return Response({'message':"subject teacher assigned successfully registered"},status=status.HTTP_200_OK)
        return Response({'message':"Error assigning subject teacher "},status=status.HTTP_400_BAD_REQUEST)
        
class SubjectTeacherList(APIView):
    def get(self,request,sem_id):
        subject_teacher = SubjectTeacher.objects.filter(subject__semester__id=sem_id)
        serializer = SubjectTeacherDetailSerializer(subject_teacher,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class CurrentBatchSemesterList(APIView):
    def get(self,request):
        batch_semester = BatchSemester.objects.filter(is_active=True,is_current=True)
        serializer = BatchSemesterDetailSerializer(batch_semester,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class BatchSemesterList(APIView):
    def get(self,request):
        batch_semester = BatchSemester.objects.filter(is_active=True)
        serializer = BatchSemesterDetailSerializer(batch_semester,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class UpgradeStudent(APIView):
    def post(self,request):
        registration_numbers = request.data['registration_number'].split(',')
        batch_semester_id = request.data['batchsemester']
        batch_semester = BatchSemester.objects.get(id=batch_semester_id)
        for reg_no in registration_numbers:
            student = Student.objects.get(registration_number = reg_no)
            prev_semesters = StudentInSemester.objects.filter(student=student)
            if not prev_semesters:
                continue
            for sem in prev_semesters:
                sem.is_current = False
                sem.save()
            in_semester = StudentInSemester.objects.create(student=student,semester=batch_semester)
            in_semester.save()
        return Response({'message':"student semester upgraded successfully"},status=status.HTTP_200_OK)
    

class AssignStudent(APIView):
    def post(self,request):
        registration_numbers = request.data['registration_number'].split(',')
        batch_semester_id = request.data['batchsemester']
        batch_semester = BatchSemester.objects.get(id=batch_semester_id)
        for reg_no in registration_numbers:
            print(reg_no)
            student = Student.objects.get(registration_number = reg_no.strip())
            in_semester = StudentInSemester.objects.create(student=student,semester=batch_semester)
            in_semester.save()
        return Response({'message':"student semester upgraded successfully"},status=status.HTTP_200_OK)


class SubjectListBatchSemester(APIView):
    def get(self,requests,batch_sem_id):
        
        batch_sem = BatchSemester.objects.get(id=batch_sem_id)
        sem_id = batch_sem.semester.id
        user = AppUser.objects.get(id=requests.user.id)

        semester = Semester.objects.get(id=sem_id, is_active=True)
        # subjects = Subject.objects.filter(semester=semester)
        subject_teacher = SubjectTeacher.objects.filter(teacher__user=user,subject__semester=semester)
        serializer = SubjectTeacherDetailSerializer(subject_teacher,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)

class StudentListBatchSemester(APIView):
    def get(self,requests,batch_sem_id):
        batch_sem = BatchSemester.objects.get(id=batch_sem_id)
        student_in_sem = StudentInSemester.objects.filter(semester=batch_sem)
        print(student_in_sem)
        serializer = StudentInSemesterSerializer(student_in_sem,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

from datetime import datetime
from django.utils import timezone
class StudentBulkAttendance(APIView):
    def post(self,request):
        print(request.data)
        subject_id = request.data['subject']
        
        attendance_date = request.data['date']
        print(attendance_date,'1')

        # date_part = attendance_date.split('T')[0]
        # print(date_part,'2')
        # date_obj = datetime.strptime(date_part, '%a %b %d %Y')
        date_obj = datetime.strptime(attendance_date, '%a %b %d %Y')
        print(date_obj,'2')

        date_obj = date_obj.strftime('%Y-%m-%d')

        print(date_obj)

        subject_obj = Subject.objects.get(id=subject_id)

        attendances = request.data['attendance']
        for st_id,st in attendances.items():
            student = Student.objects.get(id=st_id)
            print(student)
            try:
                atten_obj = StudentSubjectAttendance.objects.get(student=student,subject=subject_obj,day=date_obj)
                atten_obj.status = st
                atten_obj.save()
            except StudentSubjectAttendance.DoesNotExist:
                print("Attendance doesnot exist")
                StudentSubjectAttendance.objects.create(student=student,subject=subject_obj,day=date_obj,status=st)
        
        return Response({'message':"Attendance recorded successfully"},status=status.HTTP_200_OK)
    

class ExamTypeList(APIView):
    def get(self,request):
        exam_types = ExamType.objects.filter(is_active=True)
        serializer = ExamTypeSerializer(exam_types,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class ExamSessionList(APIView):
    def get(self,request):
        exam_session = ExamSession.objects.all()
        serializer = ExamSessionSerializer(exam_session,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class StudentStudentInternalExamMarksList(APIView):
    def post(self,request):
        print(request.data)
        subject_id = request.data['subject']
        exam_type_id = request.data['exam_type']
        # student_marks = request.data['marks']
        session_id = request.data['session_id']
        
        subj_obj = Subject.objects.get(id=subject_id)
        exam_type_obj = ExamType.objects.get(id=exam_type_id)
        exam_session_obj = ExamSession.objects.get(id=session_id)

        subject_internal_obj = SubjectInternalExam.objects.get(subject=subj_obj,exam_type=exam_type_obj)
        results = StudentInternalExamResult.objects.filter(subject_internalexam=subject_internal_obj,exam_session=exam_session_obj)
        data = {}
        for result in results:
            data[result.student.id] = float(result.marks_obtained)
        print(data)
        data = json.dumps(data)
        return Response(data,status=status.HTTP_200_OK)
    


class StudentInternalExamMarksUpdate(APIView):
    def post(self,request):
        print(request.data)
        subject_id = request.data['subject']
        exam_type_id = request.data['exam_type']
        student_marks = request.data['marks']
        session_id = request.data['session_id']

        subj_obj = Subject.objects.get(id=subject_id)
        exam_type_obj = ExamType.objects.get(id=exam_type_id)
        exam_session_obj = ExamSession.objects.get(id=session_id)

        subject_internal_obj = SubjectInternalExam.objects.get(subject=subj_obj,exam_type=exam_type_obj)
        print(subject_internal_obj)

        for s_id,marks in student_marks.items():
            st_obj = Student.objects.get(id=s_id)
            try:
                result_obj = StudentInternalExamResult.objects.get(student=st_obj,subject_internalexam=subject_internal_obj,exam_session=exam_session_obj)
                result_obj.marks_obtained = marks 
                result_obj.save()
            except Exception as e:
                print('Does not exists')
                result_obj = StudentInternalExamResult.objects.create(student=st_obj,subject_internalexam=subject_internal_obj,marks_obtained=marks,exam_session=exam_session_obj)
                result_obj.save()
        
        return Response({'message':"Marks  recorded successfully"},status=status.HTTP_200_OK)

class IndividualStudentRecord(APIView):
    def get(self,request,batch_sem_id,student_id):
        student_obj = Student.objects.get(id=student_id)
        in_semester = StudentInSemester.objects.filter(student=student_obj,is_current=True)[0]
        current_semester = in_semester.semester.semester.id
        subjects = Subject.objects.filter(semester__id=current_semester)
        records = StudentSubjectAttendance.objects.filter(student=student_obj,subject__in=subjects)
        serializer = StudentSubjectAttendanceSerializer(records,many=True)
        grouped_records = {}
        for record in serializer.data:
            if record['subject']['name'] not in grouped_records.keys():
                grouped_records[record['subject']['name']] = []
                grouped_records[record['subject']['name']].append({'day':record['day'],'status':record['status']})
            else:
                grouped_records[record['subject']['name']].append({'day':record['day'],'status':record['status']})
        # internal exam records 
        in_semester = StudentInSemester.objects.filter(student=student_obj,is_current=True)[0]
        current_semester = in_semester.semester.semester.id
        subjects = Subject.objects.filter(semester__id=current_semester)
        exam_types = ExamType.objects.all()
        records = {}
        for et in exam_types:
            for subject in subjects:
                try:
                    subject_internal = SubjectInternalExam.objects.get(subject=subject,exam_type=et)
                    sessions = ExamSession.objects.all()
                    
                    for s in sessions:
                        if s.name not in records.keys():
                            records[s.name] = []
                            exam_result = StudentInternalExamResult.objects.filter(student=student_obj,subject_internalexam=subject_internal,exam_session=s)
                            serializer = StudentInternalExamResultSerializer(exam_result,many=True)
                            records[s.name].append(serializer.data)
                        else:
                            exam_result = StudentInternalExamResult.objects.filter(student=student_obj,subject_internalexam=subject_internal,exam_session=s)
                            serializer = StudentInternalExamResultSerializer(exam_result,many=True)
                            records[s.name].append(serializer.data)
                except Exception as e:
                    continue
        data = {'attendance':grouped_records,'internal_marks':records}
        return Response(data,status=status.HTTP_200_OK)



class StudentCurrentAttendanceRecord(APIView):
    def get(self,request):
        user_id = request.user.id 
        student_obj = Student.objects.get(user__id=user_id)
        in_semester = StudentInSemester.objects.filter(student=student_obj,is_current=True)[0]
        current_semester = in_semester.semester.semester.id
        subjects = Subject.objects.filter(semester__id=current_semester)
        records = StudentSubjectAttendance.objects.filter(student=student_obj,subject__in=subjects)
        serializer = StudentSubjectAttendanceSerializer(records,many=True)
        grouped_records = {}
        for record in serializer.data:
            if record['subject']['name'] not in grouped_records.keys():
                grouped_records[record['subject']['name']] = []
                grouped_records[record['subject']['name']].append({'day':record['day'],'status':record['status']})
            else:
                grouped_records[record['subject']['name']].append({'day':record['day'],'status':record['status']})

        return Response(grouped_records,status=status.HTTP_200_OK)

class AttendanceRecordList(APIView):
    def get(self,request,subject_id):
        subject = Subject.objects.get(id=subject_id)
        records = StudentSubjectAttendance.objects.filter(subject=subject)
        serializers = StudentSubjectAttendanceDetailSerializer(records,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)


class StudentNoticeList(APIView):
    def get(self,request):
        user_id = request.user.id 
        student_obj = Student.objects.get(user__id=user_id)
        in_semester = StudentInSemester.objects.filter(student=student_obj,is_current=True)[0]
        notices = Notice.objects.filter(semester = in_semester.semester,is_active=True).order_by('-created_at')
        serializer = NoticeSerializer(notices,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    

class StudentInternalExamRecord(APIView):
    def get(self,request):
        user_id = request.user.id 
        student_obj = Student.objects.get(user__id=user_id)
        in_semester = StudentInSemester.objects.filter(student=student_obj,is_current=True)[0]
        current_semester = in_semester.semester.semester.id
        subjects = Subject.objects.filter(semester__id=current_semester)
        exam_types = ExamType.objects.all()
        records = {}
        for et in exam_types:
            for subject in subjects:
                try:
                    subject_internal = SubjectInternalExam.objects.get(subject=subject,exam_type=et)
                    sessions = ExamSession.objects.all()
                    
                    for s in sessions:
                        if s.name not in records.keys():
                            records[s.name] = []
                            exam_result = StudentInternalExamResult.objects.filter(student=student_obj,subject_internalexam=subject_internal,exam_session=s)
                            serializer = StudentInternalExamResultSerializer(exam_result,many=True)
                            records[s.name].append(serializer.data)
                        else:
                            exam_result = StudentInternalExamResult.objects.filter(student=student_obj,subject_internalexam=subject_internal,exam_session=s)
                            serializer = StudentInternalExamResultSerializer(exam_result,many=True)
                            records[s.name].append(serializer.data)
                except Exception as e:
                    continue
        return Response(records,status=status.HTTP_200_OK)
    

class SubjectTeacherListDetail(APIView):
    def get(self,request):
        teachers = Teacher.objects.filter(is_active=True)
        subject_teacher = SubjectTeacher.objects.filter(teacher__in=teachers)
        serializer = DetailSubjectTeacherSerializer(subject_teacher,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)









        










