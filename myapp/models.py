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