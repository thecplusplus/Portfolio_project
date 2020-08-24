from django.shortcuts import render
from .models import Jobs
# Create your views here.
def home(request):
    jobs = Jobs.objects
    return render(request,'homepage.html',{'jobs':jobs})
