from django.shortcuts import render
from .models import *

# Create your views here.
def index_view(request):
    heroarea = HeroArea.objects.all()
    portfolioarea = PortfolioArea.objects.all().order_by('-id')[:4]
    title = Title.objects.all()
    contex = {
        'heroarea':heroarea,
        'portfolioarea':portfolioarea,
        'title':title,
    }
    return render(request,'index.html',contex)