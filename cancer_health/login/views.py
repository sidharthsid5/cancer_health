# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import RoleModel, Patient, Guest, Volunteer
from .forms import PatientRegistrationForm, GuestRegistrationForm, VolunteerRegistrationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Home Page
def home(request):
    return redirect(login1)
    # return HttpResponse("hai<br>"
    #                     "<a href='register_patient'>Click me</a><br>"
    #                     "<a href='register_guest'>Click me</a><br>"
    #                     "<a href=' register_volunteer'>Click me</a><br>"
    #                     "<a href='login1'>Click me</a><br>"
    #                     )



    # Patient Registration
def register_patient(request):
    form = PatientRegistrationForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('Username')
            password = form.cleaned_data.get('Password')
            confirm_password = form.cleaned_data.get('ConfirmPassword')

            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Username already exists')
                else:
                    user = User.objects.create_user(username=username, password=password)
                    RoleModel.objects.create(Role='Patient', Login=user)
                    patient = form.save(commit=False)
                    patient.Login = user
                    patient.save()
                    return redirect('login1')
            else:
                messages.error(request, "Passwords do not match")

    return render(request, "register_patient.html", {'form': form})


# Guest Registration
def register_guest(request):
    form = GuestRegistrationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('Username')
            password = form.cleaned_data.get('Password')
            confirm_password = form.cleaned_data.get('ConfirmPassword')

            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Username already exists')
                else:
                    user = User.objects.create_user(username=username, password=password)
                    RoleModel.objects.create(Role='Guest', Login=user)
                    guest = form.save(commit=False)
                    guest.Login = user
                    guest.save()
                    return redirect('login1')
            else:
                messages.error(request, "Passwords do not match")

    return render(request, "register_guest.html", {'form': form})


# Volunteer Registration
def register_volunteer(request):
    form = VolunteerRegistrationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('login1')

    return render(request, "register_volunteer.html", {'form': form})



# Login
def login1(request):
    if request.method == "POST":
        usrname = request.POST.get("username")
        psword = request.POST.get("password")
        user_obj = authenticate(request, username=usrname, password=psword) # Added request to authenticate

        if user_obj is not None:
            user_id = user_obj.id

            if user_obj.is_superuser is True:
                return HttpResponseRedirect('/administrator')

            try:
                role_obj = RoleModel.objects.get(Login=user_id)
                role_type = role_obj.Role

                if role_type == 'Patient':
                    patient = Patient.objects.get(Login=user_id)
                    request.session["Patient_id"] = patient.id
                    request.session["Patient_name"] = patient.Name
                    return HttpResponseRedirect('/patient')
                elif role_type == 'Guest':
                    guest = Guest.objects.get(Login=user_id)
                    request.session["Guest_id"] = guest.id
                    request.session["Guest_name"] = guest.Name
                    return HttpResponseRedirect('/guest')
                elif role_type == 'Volunteer':
                    volunteer = Volunteer.objects.get(Login=user_id)
                    request.session["Volunteer_id"] = volunteer.id
                    request.session["Volunteer_name"] = "Volunteer"
                    return HttpResponseRedirect('/VolunteerHome')

            except RoleModel.DoesNotExist:
                messages.error(request, "User has no assigned role.")
                return redirect('login1') #redirect to log in.

        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login1') #redirect to log in.

    return render(request, 'login.html')