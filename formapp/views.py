from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

def home(request):
    context = {"courses": Courses.objects.all() }

    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        catagory = request.POST.get('catagory')
        course = request.POST.get('course')

        candidate = Candidates(name=name,phone=phone,email=email,catagory=catagory,course=course)
        candidate.save()
    
    return render(request, "home.html", context)