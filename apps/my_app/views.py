from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Course


# Create your views here.

def index(request):
    context={
        'courses': Course.objects.all()
    }
    return render(request, 'my_app/index.html', context)

def submit_course(request):
    Course.objects.create(course_name = request.POST['course_name'], description_name = request.POST['description_name'], date_name = request.POST['date_name'])
    print Course.objects.all()
    return redirect('/')

def delete_confirmation(request, id):
    
    course = Course.objects.get(id=id)

    context = {
        "course":course
    }

    return render(request, 'my_app/deleteC.html', context)


def delete_course(request, id):
    Course.objects.get(id=id).delete()
    
    return redirect('/')  