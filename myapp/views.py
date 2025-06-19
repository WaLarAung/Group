from django.shortcuts import render
from .models import *

# Create your views here.
def index_view(request):
    return render(request,'index.html')