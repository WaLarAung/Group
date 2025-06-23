from django.shortcuts import render
from .models import *

# Create your views here.
def index_view(request):
    heroarea = HeroArea.objects.all()
    portfolioarea = PortfolioArea.objects.all().order_by('-id')[:4]
    title = Title.objects.all()
    resume = Resume.objects.all()
    resume1 = Resume1.objects.all().order_by('id')[:4]
    resume2 = Resume2.objects.all().order_by('id')[:2]
    service= service1.objects.all().order_by('-id')[:1]
    service_no = service_no1.objects.all().order_by('-id')[:3]
    service_img = service_img1.objects.all().order_by('-id')[:1]
    About = about.objects.all().order_by('id')
    About1= about1.objects.all().order_by('id')[:1]
    blog_Model = Blog_Model.objects.all()
    contex = {
        'heroarea':heroarea,
        'portfolioarea':portfolioarea,
        'title':title,
        'resume':resume,
        'resume1':resume1,
        'resume2':resume2,
        'service':service,
        'service_no':service_no,
        'service_img':service_img,
        'About':About,
        'About1':About1,
        'blog_Model':blog_Model,
    }
    return render(request,'index.html',contex)