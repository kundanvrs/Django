from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.

def faculty(request):
    return render(request,'faculty/faculty.html')