from django.db import models
from django.utils.text import slugify


# Create your models here.
class AboutCollege(models.Model):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    short_name = models.CharField(max_length=255, blank=True, null=True)
    logo = models.FileField(upload_to="uploads/logo/", blank=True, null=True, default='')
    about_text = models.TextField(blank=True, null=True)
    brochure = models.FileField(upload_to="uploads/website/brochure/", blank=True, null=True)
    affiliation = models.CharField(max_length=255, blank=True, null=True)
    registration = models.CharField(max_length=255, blank=True, null=True)
    office_hourse = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    post_box = models.TextField(blank=True, null=True)
    telephone = models.TextField(blank=True, null=True)
    email_address = models.TextField(blank=True, null=True)
    google_map = models.TextField(blank=True, null=True)

    facebook = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "About College"
        verbose_name_plural = "About College"


    def __str__(self):
        return self.full_name

class CollegeChairman(models.Model):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    photo = models.FileField(upload_to="uploads/chairman/", blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    post_name = models.CharField(max_length=255, blank=True, null=True)
    text_message = models.TextField(blank=True, null=True)
    video_message = models.FileField(upload_to="uploads/website/chairman/message", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "College Chairman"
        verbose_name_plural = "College Chairman"

    def __str__(self) -> str:
        return self.full_name
    
class AccreditionAndPartnerShip(models.Model):
    heading = models.CharField(max_length=255, blank=True, null=True)
    support_text = models.TextField(blank=True, null=True)
    icon = models.FileField(upload_to="uploads/website/why/icon/", blank=True, null=True)
    order_priority = models.IntegerField(default=0,blank=True,null=True)
    def __str__(self):
        return self.heading
    class Meta:
        verbose_name = "accredition and partnership"
        verbose_name_plural = "accredition and partnership"

class HeroSection(models.Model):
    page_name = models.CharField(max_length=255,blank=True,null=True)
    heading_line = models.CharField(max_length=255,blank=True,null=True)
    support_text = models.CharField(max_length=255,blank=True,null=True)
    background_image = models.FileField(upload_to="uploads/website/bgimage/", blank=True, null=True)
    support_image = models.FileField(upload_to="uploads/website/supportimage/", blank=True, null=True)
    support_icon = models.FileField(upload_to="uploads/website/supporticon/", blank=True, null=True)
    call_to_action_1 = models.CharField(max_length=255,blank=True,null=True) 
    call_to_action_2 = models.CharField(max_length=255,blank=True,null=True) 
    call_to_action_3 = models.CharField(max_length=255,blank=True,null=True) 
    call_to_action_4 = models.CharField(max_length=255,blank=True,null=True) 
    call_to_action_5 = models.CharField(max_length=255,blank=True,null=True) 
    call_to_action_6 = models.CharField(max_length=255,blank=True,null=True) 
    call_to_action_7 = models.CharField(max_length=255,blank=True,null=True) 
    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Section"

    def __str__(self):
        return self.heading_line



class Admission(models.Model):
    intake_year = models.CharField(max_length=255,blank=True,null=True)
    deadline = models.CharField(max_length=255,blank=True,null=True)
    heading_line = models.CharField(max_length=255,blank=True,null=True)
    support_text = models.CharField(max_length=255,blank=True,null=True)
    def __str__(self):
        return self.heading_line
    class Meta:
        verbose_name = "admission"
        verbose_name_plural = "admission"

class AdmissionStep(models.Model):
    heading = models.CharField(max_length=255, blank=True, null=True)
    support_text = models.TextField(blank=True, null=True)
    icon = models.FileField(upload_to="uploads/website/why/icon/", blank=True, null=True)
    order_priority = models.IntegerField(default=0,blank=True,null=True)
    admission = models.ForeignKey(Admission,on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.heading
    class Meta:
        verbose_name = "admission step"
        verbose_name_plural = "admission step"
        ordering = ["order_priority"]



class WhySection(models.Model):
    heading_line = models.CharField(max_length=255,blank=True,null=True)
    support_text = models.CharField(max_length=255,blank=True,null=True)
    def __str__(self):
        return self.heading_line
    class Meta:
        verbose_name = "why section"
        verbose_name_plural = "why section"

class WhySectionContent(models.Model):
    heading = models.CharField(max_length=255, blank=True, null=True)
    support_text = models.TextField(blank=True, null=True)
    why_section = models.ForeignKey(WhySection,on_delete=models.CASCADE,blank=True, null=True)
    photo = models.FileField(upload_to="uploads/website/why/", blank=True, null=True)
    icon = models.FileField(upload_to="uploads/website/why/icon/", blank=True, null=True)
    order_priority = models.IntegerField(default=0,blank=True,null=True)

    class Meta:
        verbose_name = "why section content"
        verbose_name_plural = "why section content"

class LifeSection(models.Model):
    heading_line = models.CharField(max_length=255,blank=True,null=True)
    support_text = models.CharField(max_length=255,blank=True,null=True)
    video_file = models.FileField(upload_to="uploads/website/life/video/", blank=True, null=True)
    def __str__(self):
        return self.heading_line
    class Meta:
        verbose_name = "life section"
        verbose_name_plural = "life section"

class LifeSectionContent(models.Model):
    heading = models.CharField(max_length=255, blank=True, null=True)
    support_text = models.TextField(blank=True, null=True)
    life_section = models.ForeignKey(LifeSection,on_delete=models.CASCADE,blank=True, null=True)
    icon = models.FileField(upload_to="uploads/website/why/icon/", blank=True, null=True)
    order_priority = models.IntegerField(default=0,blank=True,null=True)

    class Meta:
        verbose_name = "life section content"
        verbose_name_plural = "life section content"

class Testimonial(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(upload_to='uploads/website/testimonial/', blank=True, null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)
    saying = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
    def __str__(self):
        return self.name


class Faq(models.Model):
    question_text = models.TextField()
    answer_text = models.TextField()
    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQ"
    def __str__(self) -> str:
        return self.question_text

class HomePageAccreditionAndPartnerShip(models.Model):
    accredition = models.ForeignKey(AccreditionAndPartnerShip,on_delete=models.CASCADE)
    def __str__(self):
        return self.accredition.heading
    class Meta:
        verbose_name = "homepage accredition and partnership"
        verbose_name_plural = "homepage accredition and partnership"



# about us page
class EmploymentProvider(models.Model):
    employment_by = models.CharField(max_length=255,blank=True,null=True)
    def __str__(self):
        return self.employment_by

class EmploymentProviderName(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    employment_provider = models.ForeignKey(EmploymentProvider,on_delete=models.CASCADE,blank=True, null=True)
    def __str__(self):
        return self.name

class AboutUsWhySection(models.Model):
    heading_line = models.CharField(max_length=255,blank=True,null=True)
    support_text = models.CharField(max_length=255,blank=True,null=True)
    def __str__(self):
        return self.heading_line
    class Meta:
        verbose_name = "aboutus why section"
        verbose_name_plural = "aboutus why section"

class AboutUsWhySectionContent(models.Model):
    heading = models.CharField(max_length=255, blank=True, null=True)
    support_text = models.TextField(blank=True, null=True)
    aboutus_why = models.ForeignKey(AboutUsWhySection,on_delete=models.CASCADE,blank=True, null=True)
    icon = models.FileField(upload_to="uploads/website/aboutus/why/icon/", blank=True, null=True)
    order_priority = models.IntegerField(default=0,blank=True,null=True)

    class Meta:
        verbose_name = "aboutus why section content"
        verbose_name_plural = "aboutus why section content"

class AboutUsTimeline(models.Model):
    heading_line = models.CharField(max_length=255,blank=True,null=True)
    support_text = models.CharField(max_length=255,blank=True,null=True)
    def __str__(self):
        return self.heading_line
    class Meta:
        verbose_name = "aboutus timeline"
        verbose_name_plural = "aboutus timeline"

class AboutUsTimelineContent(models.Model):
    year = models.CharField(max_length=255, blank=True, null=True)
    heading = models.CharField(max_length=255, blank=True, null=True)
    support_text = models.TextField(blank=True, null=True)
    aboutus_timeline = models.ForeignKey(AboutUsTimeline,on_delete=models.CASCADE,blank=True, null=True)
    icon = models.FileField(upload_to="uploads/website/aboutus/timeline/icon/", blank=True, null=True)
    order_priority = models.IntegerField(default=0,blank=True,null=True)
    tag_1 = models.CharField(max_length=255, blank=True, null=True)
    tag_2 = models.CharField(max_length=255, blank=True, null=True)
    tag_3 = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        verbose_name = "aboutus timeline content"
        verbose_name_plural = "aboutus timeline content"

class AboutPageAccreditionAndPartnerShip(models.Model):
    accredition = models.ForeignKey(AccreditionAndPartnerShip,on_delete=models.CASCADE)
    def __str__(self):
        return self.accredition.heading
    class Meta:
        verbose_name = "aboutpage accredition and partnership"
        verbose_name_plural = "aboutpage accredition and partnership"

# academic program 

class AcademicPrograms(models.Model):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    slogan = models.CharField(max_length=255, blank=True, null=True)
    about_program = models.CharField(max_length=255, blank=True, null=True)
    brochure = models.FileField(upload_to="uploads/website/brochure/", blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    credit = models.CharField(max_length=255, blank=True, null=True)
    current_intake = models.CharField(max_length=255, blank=True, null=True)
    total_seats = models.CharField(max_length=255, blank=True, null=True)
    total_program_fee_amount = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = "academic program"
        verbose_name_plural = "academic program"
    def __str__(self):
        return self.full_name
    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)
            # Create the slug based on the title and ID
            self.slug = slugify(f'{self.full_name}')
        super(AcademicPrograms, self).save(*args, **kwargs)

class AcademicProgramObjectives(models.Model):
    program = models.ForeignKey(AcademicPrograms,on_delete=models.CASCADE)
    objective_text = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        verbose_name = "academic program objectives"
        verbose_name_plural = "academic program objectives"
    def __str__(self):
        return self.program.full_name

class WhyAcademicProgram(models.Model):
    program = models.ForeignKey(AcademicPrograms,on_delete=models.CASCADE)
    why_text = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        verbose_name = "why program"
        verbose_name_plural = "why program"
    def __str__(self):
        return self.program.full_name
class AcademicProgramCareerProspect(models.Model):
    program = models.ForeignKey(AcademicPrograms,on_delete=models.CASCADE)
    career_text = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        verbose_name = "academic program career"
        verbose_name_plural = "academic program career"
        
    def __str__(self):
        return self.program.full_name

class AcademicProgramKeySkills(models.Model):
    program = models.ForeignKey(AcademicPrograms,on_delete=models.CASCADE)
    skill_text = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        verbose_name = "academic program skill"
        verbose_name_plural = "academic program skill"
    def __str__(self):
        return self.program.full_name

class AcademicProgramEligibility(models.Model):
    program = models.ForeignKey(AcademicPrograms,on_delete=models.CASCADE)
    eligibility_text = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        verbose_name = "academic program eligibility"
        verbose_name_plural = "academic program eligibility"
    def __str__(self):
        return self.program.full_name

class AcademicProgramEntranceExamInfo(models.Model):
    program = models.ForeignKey(AcademicPrograms,on_delete=models.CASCADE)
    entrance_text = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        verbose_name = "academic program entrance exam"
        verbose_name_plural = "academic program entrance exam"
    def __str__(self):
        return self.program.full_name

class AcademicProgramScholarship(models.Model):
    program = models.ForeignKey(AcademicPrograms,on_delete=models.CASCADE)
    scholarship_text = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        verbose_name = "academic program scholarship"
        verbose_name_plural = "academic program scholarship"
    def __str__(self):
        return self.program.full_name

class AcademicYear(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        verbose_name = "academic year"
        verbose_name_plural = "academic year"
    def __str__(self):
        return self.name

class AcademicSemester(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    total_credit = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        verbose_name = "academic sem"
        verbose_name_plural = "academic sem"
    def __str__(self):
        return self.name

class AcademicFeeStructure(models.Model):
    program = models.ForeignKey(AcademicPrograms,on_delete=models.CASCADE)
    year = models.ForeignKey(AcademicYear,on_delete=models.CASCADE)
    fee_name = models.CharField(max_length=255, blank=True, null=True)
    fee_special_text = models.CharField(max_length=255, blank=True, null=True)
    fee_amount = models.CharField(max_length=255, blank=True, null=True)
    # grand_total = models.CharField(max_length=255, blank=True, null=True)
    # notice = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name = "academic fee structure"
        verbose_name_plural = "academic fee structure"
    def __str__(self):
        return self.program.full_name


class AcademicProgramLabResource(models.Model):
    heading = models.CharField(max_length=255, blank=True, null=True)
    support_text = models.TextField(blank=True, null=True)
    program = models.ForeignKey(AcademicPrograms,on_delete=models.CASCADE)
    def __str__(self):
        return self.program.full_name
    class Meta:
        verbose_name = "Academic Program LabResource"
        verbose_name_plural = "Academic Program LabResource"

class LabResourceContent(models.Model):
    heading = models.CharField(max_length=255, blank=True, null=True)
    support_text = models.TextField(blank=True, null=True)
    icon = models.FileField(upload_to="uploads/website/lab/icon/", blank=True, null=True)
    academic_lab_resource = models.ForeignKey(AcademicProgramLabResource,on_delete=models.CASCADE,blank=True, null=True)
    order_priority = models.IntegerField(default=0,blank=True,null=True)
    def __str__(self):
        return self.heading
    class Meta:
        verbose_name = "Lab Resource Content"
        verbose_name_plural = "Lab Resource Content"

class LabResourceFeatures(models.Model):
    lab_resource_content = models.ForeignKey(LabResourceContent,on_delete=models.CASCADE,blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class AcademicIndustryPartnership(models.Model):
    heading = models.CharField(max_length=255, blank=True, null=True)
    support_text = models.TextField(blank=True, null=True)
    program = models.ForeignKey(AcademicPrograms,on_delete=models.CASCADE)
    def __str__(self):
        return self.program.full_name
    class Meta:
        verbose_name = "Academic Industry Partnership"
        verbose_name_plural = "Academic Industry Partnership"

class AcademicIndustryPartnershipContent(models.Model):
    heading = models.CharField(max_length=255, blank=True, null=True)
    support_text = models.TextField(blank=True, null=True)
    icon = models.FileField(upload_to="uploads/website/ptnr/icon/", blank=True, null=True)
    partner = models.ForeignKey(AcademicIndustryPartnership,on_delete=models.CASCADE, blank=True, null=True)
    order_priority = models.IntegerField(default=0,blank=True,null=True)
    def __str__(self):
        return self.heading
    class Meta:
        verbose_name = "Academic Industry Partnership Content"
        verbose_name_plural = "Academic Industry Partnership Content"



class AcademicCurriculum(models.Model):
    heading = models.CharField(max_length=255, blank=True, null=True)
    support_text = models.TextField(blank=True, null=True)
    program = models.ForeignKey(AcademicPrograms,on_delete=models.CASCADE)
    program_structure = models.FileField(upload_to="uploads/website/academic/structure/", blank=True, null=True)
    syllabus = models.FileField(upload_to="uploads/website/academic/syllabus/", blank=True, null=True)
    def __str__(self):
        return self.heading
    class Meta:
        verbose_name = "Academic Curriculum"
        verbose_name_plural = "Academic Curriculum"

class AcademicCourseType(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.name 
    class Meta:
        verbose_name = "academiccoursetype"
        verbose_name_plural = "academiccoursetype"


class AcademicCourse(models.Model):
    program = models.ForeignKey(AcademicPrograms,on_delete=models.CASCADE)
    year = models.ForeignKey(AcademicYear,on_delete=models.CASCADE)
    semester = models.ForeignKey(AcademicSemester,on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255, blank=True, null=True)
    course_type = models.ForeignKey(AcademicCourseType,on_delete=models.CASCADE,blank=True,null=True)
    course_code = models.CharField(max_length=255, blank=True, null=True)
    course_description = models.TextField(blank=True, null=True)
    total_credit = models.CharField(max_length=255, blank=True, null=True)
    icon = models.FileField(upload_to="uploads/website/course/icon/", blank=True, null=True)

    def __str__(self):
        return self.program.full_name
    class Meta:
        verbose_name = "Academic Course"
        verbose_name_plural = "Academic Course"


class ProgramFaq(models.Model):
    program = models.ForeignKey(AcademicPrograms,on_delete=models.CASCADE)
    question_text = models.TextField()
    answer_text = models.TextField()
    class Meta:
        verbose_name = "program FAQ"
        verbose_name_plural = "program FAQ"
    def __str__(self) -> str:
        return self.question_text

class FacultyType(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        verbose_name = "Faculty Type"
        verbose_name_plural = "Faculty Type"
    def __str__(self):
        return self.name

class FacultyCategories(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        verbose_name = "Faculty Category"
        verbose_name_plural = "Faculty Category"
    def __str__(self):
        return self.name

class FacultyExpertise(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        verbose_name = "Faculty Expertise"
        verbose_name_plural = "Faculty Expertise"
    def __str__(self):
        return self.name

class FacultyDegree(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        verbose_name = "Faculty Degree"
        verbose_name_plural = "Faculty Degree"
    def __str__(self):
        return self.name

class FacultyDesignation(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        verbose_name = "FacultyDesignation"
        verbose_name_plural = "Faculty Designation"
    def __str__(self):
        return self.name


class AcademicFaculty(models.Model):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    photo = models.FileField(upload_to="uploads/website/faculty/photo/", blank=True, null=True)
    faculty_type = models.ForeignKey(FacultyType,on_delete=models.CASCADE)
    faculty_designation = models.ForeignKey(FacultyDesignation,on_delete=models.CASCADE)
    faculty_program = models.ForeignKey(AcademicPrograms,on_delete=models.CASCADE)
    faculty_expertise = models.ForeignKey(FacultyExpertise,on_delete=models.CASCADE)
    faculty_degree = models.ForeignKey(FacultyDegree,on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Academic Faculty"
        verbose_name_plural = "Academic Faculty"
    def __str__(self):
        return self.full_name

class FacultyAssignedCourse(models.Model):
    faculty = models.ForeignKey(AcademicFaculty,on_delete=models.CASCADE)
    assigned_course = models.ForeignKey(AcademicCourse,on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Faculty Assigned Course"
        verbose_name_plural = "Faculty Assigned Course"
    def __str__(self):
        return self.faculty.full_name













    

    
























    


















