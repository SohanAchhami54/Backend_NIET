from django.db import models
from userprofile.models import *
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify




# Create your models here.
class MissionPartners(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    logo = models.FileField(upload_to="uploads/partners/",blank=True, null=True)
    def __str__(self):
        return self.name

class HomeVideo(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    video_url = models.CharField(max_length=255,blank=True,null=True)
    def __str__(self):
        return self.title
    
class HomeImages(models.Model):
    title_1 = models.CharField(max_length=255,blank=True,null=True)
    photo_1 = models.FileField(upload_to="uploads/home/image/",blank=True, null=True)
    title_2 = models.CharField(max_length=255,blank=True,null=True)
    photo_2 = models.FileField(upload_to="uploads/home/image/",blank=True, null=True)
    def __str__(self):
        return self.title_1
class Feature(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    feature_text = models.CharField(max_length=255,blank=True,null=True)
    feature_img = models.FileField(upload_to="uploads/home/feat/",blank=True, null=True)

class Home(models.Model):
    why_biomedical = CKEditor5Field('why_biomedical', config_name='extends',blank=True,null=True)
    why_photo = models.FileField(upload_to="uploads/home/image/",blank=True, null=True)
    features = models.ManyToManyField(Feature,blank=True,default='')


class AboutImages(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    photo = models.FileField(upload_to="uploads/about/image/",blank=True, null=True)
    def __str__(self):
        return self.title

class AboutCertificates(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    photo = models.FileField(upload_to="uploads/about/certificate/",blank=True, null=True)
    def __str__(self):
        return self.title

class AboutUs(models.Model):
    full_name = models.CharField(max_length=255,blank=True,null=True)
    short_name = models.CharField(max_length=255,blank=True,null=True)
    about_text = CKEditor5Field('about_text', config_name='extends',blank=True,null=True)
    logo = models.FileField(upload_to="uploads/logo/",blank=True, null=True,default='')
    about_image = models.FileField(upload_to="uploads/aboutus/",blank=True, null=True,default='')
    affiliation = models.CharField(max_length=255,blank=True,null=True)
    registration = models.CharField(max_length=255,blank=True,null=True)
    address = CKEditor5Field('address', config_name='extends',blank=True,null=True)
    post_box = CKEditor5Field('post_box', config_name='extends',blank=True,null=True)
    telephone = CKEditor5Field('telephone', config_name='extends',blank=True,null=True)
    email_address = CKEditor5Field('email_address', config_name='extends',blank=True,null=True)
    google_map = CKEditor5Field('google_map', config_name='extends',blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

class FacultyType(models.Model):
    type_name = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.type_name

class Faculty(models.Model):
    user = models.ForeignKey(AppUser,on_delete=models.CASCADE)
    user_type = models.ForeignKey(UserType,on_delete=models.CASCADE)
    # name = models.CharField(max_length=255,blank=True,null=True)
    photo = models.FileField(upload_to="uploads/faculty/",blank=True, null=True)
    education = models.CharField(max_length=255,blank=True,null=True)
    designation = models.CharField(max_length=255,blank=True,null=True)
    post_name = models.CharField(max_length=255,blank=True,null=True)
    # email = models.CharField(max_length=255,blank=True,null=True)
    faculty_type = models.ForeignKey(FacultyType,on_delete=models.CASCADE,blank=True,null=True)
    linkedin_url = models.CharField(max_length=255,blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.user.first_name

class Chairman(models.Model):
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    message = CKEditor5Field('message', config_name='extends',blank=True,null=True)
    def __str__(self) -> str:
        return self.faculty.user.first_name



# models for project and its category 

class ProjectCategory(models.Model):
    type_name = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.type_name



# models for news 
class News(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    content = CKEditor5Field('content', config_name='extends')
    photo = models.FileField(upload_to="uploads/news/",blank=True, null=True)
    pdf = models.FileField(upload_to="uploads/news/pdf/",blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)
            # Create the slug based on the title and ID
            self.slug = slugify(f'{self.title}-{self.id}')
        super(News, self).save(*args, **kwargs)

class Vaccancy(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    content = CKEditor5Field('content', config_name='extends')
    photo = models.FileField(upload_to="uploads/vaccancy/",blank=True, null=True)
    pdf = models.FileField(upload_to="uploads/vaccancy/pdf/",blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    display_as_new = models.BooleanField(default=True,blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)
            # Create the slug based on the title and ID
            self.slug = slugify(f'{self.title}-{self.id}')
        super(Vaccancy, self).save(*args, **kwargs)

class NoticeAndResult(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    content = CKEditor5Field('content', config_name='extends')
    photo = models.FileField(upload_to="uploads/notice/",blank=True, null=True)
    pdf = models.FileField(upload_to="uploads/notice/pdf/",blank=True, null=True)
    any_url = models.CharField(max_length=255,blank=True,null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    display_as_new = models.BooleanField(default=True,blank=True,null=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)
            # Create the slug based on the title and ID
            self.slug = slugify(f'{self.title}-{self.id}')
        super(NoticeAndResult, self).save(*args, **kwargs)


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    message = CKEditor5Field('message', config_name='extends')

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'contact messages'

    def __str__(self):
        return self.first_name

class Faq(models.Model):
    question_text = CKEditor5Field('question_text', config_name='extends')
    answer_text = CKEditor5Field('answer_text', config_name='extends')
    def __str__(self) -> str:
        return self.question_text
    
class Gallery(models.Model):
    description = CKEditor5Field('description', config_name='extends')
    photo = models.ImageField(upload_to='uploads/gallery/', blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'galleries'

    def __str__(self):
        return self.description
























