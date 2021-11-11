from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def About(request):
    return render(request,'about.html',{})

def Home(request):
    return render(request,'home.html',{})

def Contact(request):
    return render(request,'contact.html',{})


def handleSignUp(request):
    if request.method == 'POST':
        #GET THE POST PARAMETERS
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
     # check for errorneous input
        if len(username)> 10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')


     # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your LivLyf has been successfully created")
        return redirect('home')
    else:
        return HttpResponse('404- Page Not Found')


def handleLogin(request):
    if request.method == 'POST':
        #GET THE POST PARAMETERS
        loginusername=request.POST['username']
        loginpass=request.POST['pass']
        user=authenticate(username= loginusername, password= loginpass)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")


    return HttpResponse("404- Not found")

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')