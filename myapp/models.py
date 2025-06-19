from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class HeroArea(models.Model):
    title = RichTextField(null=True,blank=True)
    note = models.TextField(null=True,blank=True)
    description = models.TextField()
    bgimage = models.ImageField(upload_to='heroares',null=True,blank=True)
