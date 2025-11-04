from student_management.models import *

university,created = University.objects.get_or_create(name="Purbanchal University (PU)")
degree,created = Degree.objects.get_or_create(name="Biomedical Engineering (BME)")

sections = ["A","B","C","D"]
for section in sections:
    sec,created = Section.objects.get_or_create(name=section)

university_degree,created = UniversityDegree.objects.get_or_create(degree=degree,university=university)

batches = ["Batch-17","Batch-18","Batch-19",
           "Batch-20","Batch-21","Batch-22","Batch-23","Batch-24","Batch-25",
           "Batch-26","Batch-27","Batch-28","Batch-29","Batch-30"
           ]
for year in batches:
    academic_batch,created = AcademicBatch.objects.get_or_create(year=year)
    degree_batch,created = DegreeBatch.objects.get_or_create(university_degree=university_degree,academic_batch=academic_batch)

semesters_num = ['1','2','3','4','5','6','7','8']
for number in semesters_num:
    academic_semester,created = AcademicSemester.objects.get_or_create(number=number)







