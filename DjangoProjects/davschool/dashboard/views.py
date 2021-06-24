from django.shortcuts import render,HttpResponse,redirect,get_object_or_404

# Create your views here.

def HomePage(request):
    return render(request,'dashboard/homepage.html')

def handleLogin(request):
    return render(request,'dashboard/handlelogin.html')

def handleLogout(request):
    return render(request,'dashboard/handlelogout.html')

def handleSignup(request):
    return render(request,'dashboard/handlesignup.html')

