from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.

def student(request):
    return render(request,'student/student.html')