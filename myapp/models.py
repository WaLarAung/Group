from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class HeroArea(models.Model):
    title = RichTextField(null=True,blank=True)
    note = models.TextField(null=True,blank=True)
    description = models.TextField()
    bgimage = models.ImageField(upload_to='heroares',null=True,blank=True)

class PortfolioArea(models.Model):
    title =  RichTextField(null=True,blank=True)
    name = RichTextField(null=True,blank=True)
    description = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='portfolioarea',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Title(models.Model):
    title = RichTextField(null=True,blank=True)
    description = models.TextField(null=True, blank=True)

class Resume(models.Model):
    title = RichTextField(null=True,blank=True)
    description = RichTextField(null=True,blank=True)
    note = RichTextField(null=True,blank=True)
    title1 = RichTextField(null=True,blank=True)
    title2 = RichTextField(null=True,blank=True)
    image = models.ImageField(upload_to='resume',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Resume1(models.Model):
    title = RichTextField(null=True,blank=True)
    note = RichTextField(null=True,blank=True)
    description = RichTextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Resume2(models.Model):
    title = RichTextField(null=True,blank=True)
    experience = RichTextField(null=True,blank=True)
    position = RichTextField(null=True,blank=True)
    description = RichTextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class service1(models.Model):
    name = RichTextField(max_length=300)
    title = RichTextField(max_length=100)
    description = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class service_no1(models.Model):
    no = RichTextField(max_length=400)
    description = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class service_img1(models.Model):
    image = models.ImageField(upload_to='service/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class about(models.Model):
    name= RichTextField(null=True,blank=True)
    title= RichTextField(null=True,blank=True)
    description = RichTextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class about1(models.Model):
    title = RichTextField(null=True,blank=True)
    description = RichTextField(null=True,blank=True)
    image = models.ImageField(upload_to='about')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
