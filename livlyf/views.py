from datetime import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from .models import Appoin, Center_Vaccine_reln, Vaccine_detail, Hospital, Vaccination_Center,Patient,Personal_Detail

from .forms import Registration, Feedback

from .filter1 import OrderFilter,OrderFilterV,OrderFilterC,OrderFilterP
# Create your views here.
def CenterInfo(request):
    Reln=Center_Vaccine_reln.objects.all()
    return render(request,'centerinfo.html',{'re':Reln})

def Appointment(request):
    if request.method == 'POST':
        adhar=request.user.username
        v_chos=request.POST['vaccines']
        num=request.POST['num']
        date=request.POST['date']
        time=request.POST['time']
        Appoin.objects.create(Name=adhar,Date=date,Vaccine=v_chos,Number=num)
        messages.success(request,"Form Created Successfully") 
        redirect('home')  
    
    try:
        one_entry = Personal_Detail.objects.get(pk=request.user)
    except Personal_Detail.DoesNotExist:
        one_entry = None
    m=Vaccine_detail.objects.all()
    if request.user.is_authenticated and one_entry:
        return render(request,'appointment.html',{'u':one_entry,'vacc':m,})
    elif request.user.is_authenticated:
        messages.error(request, "Please Register First")
        return redirect('registration')
    else:
        return HttpResponse("Log-In to book appointment")

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
        try:
            user_exists = User.objects.get(username=username)
            messages.error(request, "Aadhar Number already register")
            return redirect('home')
        except User.DoesNotExist:
     # check for errorneous input
            if len(username)!= 12:
                messages.error(request, "Aadhar Number should be 12 Digit long")
                return redirect('home')

            if not username.isnumeric():
                messages.error(request, " User name should only contain numbers")
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

def Vaccines(request):
    vacc=Vaccine_detail.objects.all()
    myFilter=OrderFilterV(request.GET,queryset=vacc)
    vacc=myFilter.qs
    return render(request,'vaccine.html',{'vacc':vacc,'myFilter':myFilter})

def Hospitals(request):
    cat=request.GET.get('orderby')
    hosp=Hospital.objects.all()
    myFilter=OrderFilter(request.GET,queryset=hosp)
    hosp=myFilter.qs
    print("hello")
    print(cat)
    return render(request,'hospital.html',{'hosp':hosp,'myFilter':myFilter})

def Centers(request):
    Center=Vaccination_Center.objects.all()
    myFilter=OrderFilterC(request.GET,queryset=Center)
    Center=myFilter.qs
    return render(request,'centers.html',{'Center':Center,'myFilter':myFilter})

def Patients(request):
    if request.user.is_staff:
        pat=Patient.objects.all()
        myFilter=OrderFilterP(request.GET,queryset=pat)
        pat=myFilter.qs

        Hos=Hospital.objects.all()
        Per=Personal_Detail.objects.all()
        # hosp=Hospital.obejects.get(pk=pat.Hospital_ID_id)
        return render(request,'patient.html',{'pat':pat,'myFilter':myFilter,'Hos':Hos,'Per':Per})
    else:
            return HttpResponse("404- Not found")

def Profile(request):
    try:
        one_entry = Personal_Detail.objects.get(pk=request.user)
    except Personal_Detail.DoesNotExist:
        one_entry = None
    
    if request.user.is_authenticated and one_entry:
        return render(request,'profile.html',{'u':one_entry})
    elif request.user.is_authenticated:
        messages.error(request, "Please Register First")
        return redirect('registration')
    else:
        return HttpResponse("404- Not found")

def Registrations(request):
    if request.method == 'POST': 
        form = Registration(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.Aadhar_number=request.user
            post.Email_ID=request.user.email
            post.save()
            messages.success(request, "Successfully register")
        else:
            messages.error(request,"Invalid Form")
        return redirect('home')  
    else:
        form = Registration()
    return render(request,'registration.html',{'form':form})

def Home(request):
        count=0
        form = Feedback()
        if request.method == 'POST': 
            if 'button1' in request.POST:
                form = Feedback(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request,"Feedack submitted Sucessfuly")
                return redirect('home')            
        else:
            form=Feedback()
            nos= 'No data available'
            

        return render(request, 'home.html', {'form': form,'nos':count})