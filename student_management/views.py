import random
import csv
import pandas as pd
from bs4 import BeautifulSoup
from django.shortcuts import render
from student_management.models import *
from student_management.serializers import *
from userprofile.models import *

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

class UniversityDetail(APIView):
    def get(self,request):
        object = University.objects.filter(is_active=True)
        serializer = UniversitySerializer(object,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class DegreeDetail(APIView):
    def get(self,request):
        object = Degree.objects.filter(is_active=True)
        serializer = DegreeSerializer(object,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class AcademicBatchDetail(APIView):
    def get(self,request):
        object = AcademicBatch.objects.filter(is_active=True)
        serializer = AcademicBatchSerializer(object,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class AcademicSemesterDetail(APIView):
    def get(self,request):
        object = AcademicSemester.objects.filter(is_active=True)
        serializer = AcademicSemesterSerializer(object,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class ExternalExamTypeDetail(APIView):
    def get(self,request):
        object = ExternalExamType.objects.filter(is_active=True)
        serializer = ExternalExamTypeSerializer(object,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class ExternalExamResultList(APIView):
    def get(self,request):
        object = ExternalExamResult.objects.all()
        serializer = ExternalExamResultSerializer(object,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class ExternalExamResultDetail(APIView):
    def get(self,request,id):
        external_exam_result = ExternalExamResult.objects.get(id=id)
        result_content = ExternalExamResultContent.objects.filter(result_meta=external_exam_result)
        result_content_serializer = ExternalExamResultContentSerializer(result_content,many=True)
        result_scores = ExternalExamResultScore.objects.filter(external_result_content__in=result_content)
        result_scores_serializer = ExternalExamResultScoreSerializer(result_scores,many=True)

        content_df = pd.DataFrame(result_content_serializer.data)
        scores_df = pd.DataFrame(result_scores_serializer.data)

        print(content_df.head())
        print(scores_df.head())
        
        merged_df = content_df.merge(scores_df, left_on="id", right_on="external_result_content", how="left")
        # merged_df = pd.concat()
        # print(merged_df.head(10))


        
        # Group subjects and scores into a list of dictionaries per student
        result = merged_df.groupby(["id_x", "symbol_number", "registration_number", "student_name", "sgpa", "pass_fail", "result_meta"]).apply(
            lambda x: {
                "id": x.name[0],
                "symbol_number": x.name[1],
                "registration_number": x.name[2],
                "student_name": x.name[3],
                "sgpa": x.name[4],
                "pass_fail": x.name[5],
                "result_meta": x.name[6],
                **{row["subject"]: row["score"] for _, row in x.iterrows()}  # Unpacking subjects directly
            }
        ).tolist()

        return Response(result,status=status.HTTP_200_OK)

class ExternalOriginalExamResultDetail(APIView):
    def get(self,request,id):
        external_exam_result = ExternalExamResult.objects.get(id=id)
        file_path = external_exam_result.original_result_record.path
        with open(file_path, "r", encoding="utf-8") as file:
            html_content = file.read()
        print(type(html_content))
        return Response({"html_content": html_content}, status=status.HTTP_200_OK)





class StudentBatchSemesterList(APIView):
    def post(self,request):
        data = request.data
        university = University.objects.get(id=data['university'])
        degree = Degree.objects.get(id=data['degree'])
        academic_batch = AcademicBatch.objects.get(id=data['academic_batch'])
        academic_semester = AcademicSemester.objects.get(id=data['academic_semester'])
        print(data)
        try:
            university_degree = UniversityDegree.objects.get(
                degree = degree,
                university= university
            )
            degree_batch = DegreeBatch.objects.get(
                university_degree = university_degree,
                academic_batch = academic_batch
            )
            batch_semester = BatchSemester.objects.get(
                degree_batch = degree_batch,
                academic_semester = academic_semester
            )
        except Exception as e:
            return Response({'message':e},status=status.HTTP_400_BAD_REQUEST)
        
        
        student_batch_semester=  StudentBatchSemester.objects.filter(
            batch_semester = batch_semester
        )
        serializer = StudentBatchSemesterSerializer(student_batch_semester,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)



class RegisterStudent(APIView):
    parser_classes = [MultiPartParser,FormParser]
    def post(self,request):
        serializer = StudentRegisterSerializer(data=request.data)
        if serializer.is_valid():
            excel_file = serializer.validated_data['excel_file']
            df = pd.read_excel(excel_file,header=0).reset_index()
            records = df.to_dict('records')
            data = serializer.data
            university = University.objects.get(id=data['university'])
            degree = Degree.objects.get(id=data['degree'])
            academic_batch = AcademicBatch.objects.get(id=data['academic_batch'])
            academic_semester = AcademicSemester.objects.get(id=data['academic_semester'])

            for record in records:
                print(record)
                try:
                    first_name = record.get('FirstName', '').strip()
                    last_name = record.get('LastName', '').strip()
                    email_address = record.get('EmailAddress', '').strip()
                    registration_num = record.get('Registration', '').strip()
                except Exception as e:
                    return Response({'message':f'Please correct error at index: {record.get('index')+1}'},status=status.HTTP_400_BAD_REQUEST)
                
                student_obj = Student.objects.filter(registration_number=registration_num)
                if not email_address and first_name and last_name and registration_num:
                    return Response({'message':f'Please correct error at index: {record.get('index')+1}'},status=status.HTTP_400_BAD_REQUEST)
                if student_obj:
                    return Response({'message':f'Please correct error at index: {record.get('index')+1} Email already exists'},status=status.HTTP_400_BAD_REQUEST)
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
                    try:
                        university_degree = UniversityDegree.objects.get(
                            degree = degree,
                            university= university
                        )
                        degree_batch = DegreeBatch.objects.get(
                            university_degree = university_degree,
                            academic_batch = academic_batch
                        )
                        batch_semester = BatchSemester.objects.get(
                            degree_batch = degree_batch,
                            academic_semester = academic_semester
                        )
                        student_batch_semester,created =  StudentBatchSemester.objects.get_or_create(
                            student = student,
                            batch_semester = batch_semester
                        )
                    except Exception as e:
                        return Response({'message':e},status=status.HTTP_400_BAD_REQUEST)
            return Response({'status':'success'},status=status.HTTP_201_CREATED)

class UploadExternalExamResult(APIView):
    def post(self,request):
        serializer = ExternalExamResultSerializer(data=request.data)
        if serializer.is_valid():
            external_exam_result = serializer.save()
            excel_file = serializer.validated_data['result_record']
            df = pd.read_excel(excel_file,header=0)
            records = df.values.tolist()
            subjects = list(df.columns[4:-2])
            print(records[0])
            
            for record in records:
                info_record = record[1:4]
                marks_record = record[4:-2]
                sgpa = record[-2]
                pass_fail = record[-1]
                
                result_content = ExternalExamResultContent.objects.create(
                    result_meta = external_exam_result,
                    symbol_number = info_record[0],
                    registration_number = info_record[1],
                    student_name = info_record[2],
                    sgpa = sgpa,
                    pass_fail = pass_fail
                )
                for i in range(len(marks_record)):
                    result_score = ExternalExamResultScore.objects.create(
                        external_result_content = result_content,
                        subject = subjects[i],
                        score = marks_record[i]
                    )
            return Response({'status':'success'},status=status.HTTP_201_CREATED)

class StudentDetail(APIView):
    def get(self,request,user_id):
        user = AppUser.objects.get(id=user_id)
        student = Student.objects.get(user=user)
        serializer = StudentViewSerializer(student)
        batch_semester_obj = StudentBatchSemester.objects.filter(student=student,batch_semester__is_running=True)[0]
        batch_serializer = StudentBatchSemesterBaseSerializer(batch_semester_obj)
        return Response({'student':serializer.data,'batch':batch_serializer.data},status=status.HTTP_200_OK)

class StudentExternalResultDetail(APIView):
    def get(self,request,user_id):
        user = AppUser.objects.get(id=user_id)
        student = Student.objects.get(user=user)
        content_obj = ExternalExamResultContent.objects.filter(registration_number=student.registration_number)
        result_score = ExternalExamResultScore.objects.filter(external_result_content__in=content_obj)
        serializer = ExternalExamResultScoreDetailSerializer(result_score,many=True)
        print(serializer.data)
        content = []
        for data in serializer.data:
            content.append({
                'id':data['id'],
                'subject':data['subject'],
                'score':data['score'],
                'registration_number':data['external_result_content']['registration_number'],
                'pass_fail':data['external_result_content']['pass_fail'],
                'sgpa':data['external_result_content']['sgpa'],
                'exam_type':data['external_result_content']['result_meta']['exam_type'],
                'result_meta':data['external_result_content']['result_meta']['id'],
                'examination_held_on':data['external_result_content']['result_meta']['examination_held_on'],
                'result_published_date':data['external_result_content']['result_meta']['result_published_date'],
                'year_semester':data['external_result_content']['result_meta']['year_semester']
            })
        
        df = pd.DataFrame(content)
        # print(df.iloc[0].values)
        grouped_data = (
            df.groupby("result_meta")
            .apply(lambda g: {
                "id": g["id"].min(), 
                **{row["subject"]: row["score"] for _, row in g.iterrows()},  
                "sgpa": g["sgpa"].iloc[0],  
                "pass_fail": g["pass_fail"].iloc[0],  
                "exam_type": g["exam_type"].iloc[0],
                "examination_held_on": g["examination_held_on"].iloc[0],
                "result_published_date": g["result_published_date"].iloc[0],
            })
            .tolist()
        )
        return Response({'original':df.to_dict(orient='records'),'grouped':grouped_data},status=status.HTTP_200_OK)

# for semester notices 
class BatchSemesterNoticeCreate(APIView):
    def post(self,request):
        data = request.data
        print(data)
        university = University.objects.get(id=data['university'])
        degree = Degree.objects.get(id=data['degree'])
        academic_batch = AcademicBatch.objects.get(id=data['academic_batch'])
        academic_semester = AcademicSemester.objects.get(id=data['academic_semester'])
        try:
            university_degree = UniversityDegree.objects.get(
                degree = degree,
                university= university
            )
            degree_batch = DegreeBatch.objects.get(
                university_degree = university_degree,
                academic_batch = academic_batch
            )
            batch_semester_obj = BatchSemester.objects.get(
                degree_batch = degree_batch,
                academic_semester = academic_semester
            )
        except Exception as e:
            return Response({'message':e},status=status.HTTP_400_BAD_REQUEST)

        serializer = BatchSemesterNoticeCreateSerializer(
            data={
                "batch_semester": batch_semester_obj.id,
                "title":data['title'],
                "messages": data["messages"],
                "attachment": data["attachment"] if "attachment" in data else None
                }
        )
        if serializer.is_valid():
            notice = serializer.save()
            return Response({'message':"Notice created sucessfully"},status=status.HTTP_200_OK)
        
        return Response({'message':"Errror while creating notice"},status=status.HTTP_400_BAD_REQUEST)

class SemesterNoticeList(APIView):
    def get(self,request):
        notices = BatchSemesterNotice.objects.filter(is_active=True).order_by('-created_at')
        serializer = BatchSemesterNoticeDetailSerializer(notices,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class SemesterNoticeDetail(APIView):
    def get(self,request,id):
        notices = BatchSemesterNotice.objects.get(id=id)
        serializer = BatchSemesterNoticeDetailSerializer(notices)
        return Response(serializer.data,status=status.HTTP_200_OK)

class StudentNoticeList(APIView):
        def get(self,request,user_id):
            user = AppUser.objects.get(id=user_id)
            student = Student.objects.get(user=user)
            serializer = StudentViewSerializer(student)
            batch_semester_obj = StudentBatchSemester.objects.filter(student=student,batch_semester__is_running=True)[0]
            notices = BatchSemesterNotice.objects.filter(batch_semester=batch_semester_obj.batch_semester).order_by('-created_at')
            serializer = BatchSemesterNoticeDetailSerializer(notices,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)


        




            

        



