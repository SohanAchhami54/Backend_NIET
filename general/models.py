from django.db import models
from userprofile.models import *
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify

# Create your models here.

# # need to be deleted 
# class MissionPartners(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True)
#     logo = models.FileField(upload_to="uploads/partners/", blank=True, null=True)

#     class Meta:
#         verbose_name = "Mission Partner"
#         verbose_name_plural = "Mission Partners"

#     def __str__(self):
#         return self.name

# # need to be deleted 
# class HomeVideo(models.Model):
#     title = models.CharField(max_length=255, blank=True, null=True)
#     video_url = models.CharField(max_length=255, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_active = models.BooleanField(default=True)

#     class Meta:
#         verbose_name = "Home Video"
#         verbose_name_plural = "Home Videos"

#     def __str__(self):
#         return self.title

class CoverImage(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    photo = models.FileField(upload_to="uploads/home/cover/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Cover Image"
        verbose_name_plural = "Cover Images"

    def __str__(self):
        return self.title_1

class ModalImage(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    photo = models.FileField(upload_to="uploads/home/modal/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Modal Image"
        verbose_name_plural = "Modal Images"



class SliderHome(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    photo = models.FileField(upload_to="uploads/home/slider/image/", blank=True, null=True)
    content  = models.TextField(blank=True, null=True)
    order_priority = models.IntegerField(default=0,blank=True,null=True)

    # content  = CKEditor5Field('content_1', config_name='extends', blank=True, null=True)
    class Meta:
        verbose_name = "Slider Home"
        verbose_name_plural = "Slider Home"

    def __str__(self):
        return self.title
    
# # need to be deleted 
# class HomeImages(models.Model):
#     title_1 = models.CharField(max_length=255, blank=True, null=True)
#     photo_1 = models.FileField(upload_to="uploads/home/image/", blank=True, null=True)
#     title_2 = models.CharField(max_length=255, blank=True, null=True)
#     photo_2 = models.FileField(upload_to="uploads/home/image/", blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_active = models.BooleanField(default=True)

#     class Meta:
#         verbose_name = "Home Image"
#         verbose_name_plural = "Home Images"

#     def __str__(self):
#         return self.title_1

class Feature(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    feature_text = models.TextField(blank=True, null=True)
    feature_img = models.FileField(upload_to="uploads/home/feat/", blank=True, null=True)
    order_priority = models.IntegerField(default=0,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Feature"
        verbose_name_plural = "Features"

# # need to be deleted 
# class Home(models.Model):
#     why_biomedical = CKEditor5Field('why_biomedical', config_name='extends', blank=True, null=True)
#     why_photo = models.FileField(upload_to="uploads/home/image/", blank=True, null=True)
#     features = models.ManyToManyField(Feature, blank=True, default='')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_active = models.BooleanField(default=True)

#     class Meta:
#         verbose_name = "Home"
#         verbose_name_plural = "Homes"

# # need to be deleted 
# class AboutImages(models.Model):
#     title = models.CharField(max_length=255, blank=True, null=True)
#     photo = models.FileField(upload_to="uploads/about/image/", blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_active = models.BooleanField(default=True)

#     class Meta:
#         verbose_name = "About Image"
#         verbose_name_plural = "About Images"

#     def __str__(self):
#         return self.title

# # need to be deleted 
# class AboutCertificates(models.Model):
#     title = models.CharField(max_length=255, blank=True, null=True)
#     photo = models.FileField(upload_to="uploads/about/certificate/", blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_active = models.BooleanField(default=True)

#     class Meta:
#         verbose_name = "About Certificate"
#         verbose_name_plural = "About Certificates"

#     def __str__(self):
#         return self.title

class AboutUs(models.Model):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    short_name = models.CharField(max_length=255, blank=True, null=True)
    about_text = CKEditor5Field('about_text', config_name='extends', blank=True, null=True)
    logo = models.FileField(upload_to="uploads/logo/", blank=True, null=True, default='')
    about_image = models.FileField(upload_to="uploads/aboutus/", blank=True, null=True, default='')
    video_url = models.CharField(max_length=255, blank=True, null=True)
    affiliation = models.CharField(max_length=255, blank=True, null=True)
    registration = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    post_box = models.TextField(blank=True, null=True)
    telephone = models.TextField(blank=True, null=True)
    email_address = models.TextField(blank=True, null=True)
    google_map = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"

    def __str__(self):
        return self.full_name


class StaffType(models.Model):
    type_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Staff Type"
        verbose_name_plural = "Staff Types"

    def __str__(self):
        return self.type_name

class Staff(models.Model):
    JOB_CHOICES = [
        ("1","full time"),
        ("2","visiting")
    ]
    full_name = models.CharField(max_length=255, blank=True, null=True)
    photo = models.FileField(upload_to="uploads/faculty/", blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    post_name = models.CharField(max_length=255, blank=True, null=True)
    job_type = models.TextField(choices=JOB_CHOICES, blank=True, null=True)
    staff_type = models.ForeignKey(StaffType, on_delete=models.CASCADE, blank=True, null=True)
    order_priority = models.IntegerField(default=0,blank=True,null=True)
    linkedin_url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"

    def __str__(self):
        return self.full_name

# class Chairman(models.Model):
#     staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
#     message = CKEditor5Field('message', config_name='extends', blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_active = models.BooleanField(default=True)

#     class Meta:
#         verbose_name = "Chairman"
#         verbose_name_plural = "Chairmen"

#     def __str__(self) -> str:
#         return self.staff.full_name

class CollegeChairman(models.Model):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    photo = models.FileField(upload_to="uploads/chairman/", blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    post_name = models.CharField(max_length=255, blank=True, null=True)
    message = CKEditor5Field('message', config_name='extends', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "College Chairman"
        verbose_name_plural = "College Chairman"

    def __str__(self) -> str:
        return self.full_name

# models for syllabus 
class Syllabus(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = CKEditor5Field('syllabus content', config_name='extends', blank=True, null=True)
    pdf = models.FileField(upload_to="uploads/syllabus/pdf/", blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Syllabus"
        verbose_name_plural = "Syllabus"

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)
            # Create the slug based on the title and ID
            self.slug = slugify(f'{self.title}-{self.id}')
        super(Syllabus, self).save(*args, **kwargs)


class EntranceSyllabus(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = CKEditor5Field('entrance syllabus content', config_name='extends', blank=True, null=True)
    pdf = models.FileField(upload_to="uploads/entrance/syllabus/pdf/", blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Entrance Syllabus"
        verbose_name_plural = "Entrance Syllabus"

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)
            # Create the slug based on the title and ID
            self.slug = slugify(f'{self.title}-{self.id}')
        super(EntranceSyllabus, self).save(*args, **kwargs)

class EligiblityCriteria(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = CKEditor5Field('eligiblity content', config_name='extends', blank=True, null=True)
    pdf = models.FileField(upload_to="uploads/eligiblity/pdf/", blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Eligiblity Criteria"
        verbose_name_plural = "Eligiblity Criteria"

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)
            # Create the slug based on the title and ID
            self.slug = slugify(f'{self.title}-{self.id}')
        super(EligiblityCriteria, self).save(*args, **kwargs)

# models for project and its category 
class ProjectCategory(models.Model):
    type_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Project Category"
        verbose_name_plural = "Project Categories"

    def __str__(self):
        return self.type_name

# models for news 
class News(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = CKEditor5Field('content', config_name='extends')
    photo = models.FileField(upload_to="uploads/news/", blank=True, null=True)
    pdf = models.FileField(upload_to="uploads/news/pdf/", blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    scroll = models.BooleanField(default=False)
    redirect_to_url = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)
            # Create the slug based on the title and ID
            self.slug = slugify(f'{self.title}-{self.id}')
        super(News, self).save(*args, **kwargs)

class Vaccancy(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = CKEditor5Field('content', config_name='extends')
    photo = models.FileField(upload_to="uploads/vaccancy/", blank=True, null=True)
    pdf = models.FileField(upload_to="uploads/vaccancy/pdf/", blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    display_as_new = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)
            # Create the slug based on the title and ID
            self.slug = slugify(f'{self.title}-{self.id}')
        super(Vaccancy, self).save(*args, **kwargs)

class Notice(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = CKEditor5Field('content', config_name='extends')
    photo = models.FileField(upload_to="uploads/notice/", blank=True, null=True)
    pdf = models.FileField(upload_to="uploads/notice/pdf/", blank=True, null=True)
    any_url = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    display_as_new = models.BooleanField(default=True, blank=True, null=True)
    scroll = models.BooleanField(default=False)
    redirect_to_url = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Notice"
        verbose_name_plural = "Notices"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)
            # Create the slug based on the title and ID
            self.slug = slugify(f'{self.title}-{self.id}')
        super(Notice, self).save(*args, **kwargs)

class Result(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = CKEditor5Field('content', config_name='extends')
    photo = models.FileField(upload_to="uploads/result/", blank=True, null=True)
    pdf = models.FileField(upload_to="uploads/notice/pdf/", blank=True, null=True)
    any_url = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    display_as_new = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Result"
        verbose_name_plural = "Results"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)
            # Create the slug based on the title and ID
            self.slug = slugify(f'{self.title}-{self.id}')
        super(Result, self).save(*args, **kwargs)

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = CKEditor5Field('message', config_name='extends')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return self.full_name

class Faq(models.Model):
    question_text = CKEditor5Field('question_text', config_name='extends')
    answer_text = CKEditor5Field('answer_text', config_name='extends')

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self) -> str:
        return self.question_text
    
class Gallery(models.Model):
    description = CKEditor5Field('description', config_name='extends')
    photo = models.ImageField(upload_to='uploads/gallery/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"

    def __str__(self):
        return self.description

class Testimonial(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(upload_to='uploads/testimonial/', blank=True, null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return self.name

class VideoTestimonial(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)
    video_url = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Video Testimonial"
        verbose_name_plural = "Video Testimonials"

    def __str__(self):
        return self.name

# college alumni 

class Alumni(models.Model):
    # Basic Information
    full_name = models.CharField(max_length=1255)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    # Academic Information
    batch = models.CharField(max_length=15, blank=True, null=True)
    department = models.CharField(max_length=150)
    
    # Professional Information
    current_position = models.CharField(max_length=150)  # New Field
    company_name = models.CharField(max_length=150, blank=True, null=True)
    current_occupation = models.CharField(max_length=150, blank=True, null=True)  
    achievements = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    
    # Personal Message
    message = models.TextField(blank=True, null=True, help_text="A message or advice from the alumni.")  # New Field
    
    # Media
    profile_picture = models.ImageField(upload_to='alumni_pictures/', blank=True, null=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Alumni"
        ordering = ['batch', 'full_name']

    def __str__(self):
        return f"{self.full_name}  ({self.batch})"

    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)
            self.slug = slugify(f'{self.full_name.replace(" ","-")}-{self.id}')
        super(Alumni, self).save(*args, **kwargs)



