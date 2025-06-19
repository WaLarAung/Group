from django.shortcuts import render
from .models import *

# Create your views here.
def index_view(request):
    heroarea = HeroArea.objects.all()
    contex = {
        'heroarea':heroarea,
    }
    return render(request,'index.html',contex)