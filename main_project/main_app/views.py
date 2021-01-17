from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import User, Patient, Institution
from django.contrib.auth.forms import AuthenticationForm
from .forms import PatientRegistrationForm, InstitutionRegistrationForm
from .serializers import UserSerializer, PatientSerializer, InstitutionSerializer
from rest_framework import generics

def home(request):
    return render(request, 'main_app/home.html')

def login_patient(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        email = request.POST['username']
        password = request.POST['password']
        patient = authenticate(username = email, password = password)
        print(patient)
        if patient:
            print("HERE!")
            login(request, patient.user)
            return redirect('frontend-index')
        else:
            messages.error(request, f'Incorrect email or password')
            return redirect('accounts-login-patient')
    else:
        form = AuthenticationForm()

    context = {
        'form' : form
    }

    return render(request, 'main_app/login.html', context)

def register_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = User(username = form.instance.email, is_patient = True, name = form.instance.first_name)
            user.save()
            form.instance.user = user
            form.instance.save()
            form.save()
            messages.success(request, f'Account created! You may now log in.')
            return redirect('accounts-login-patient')
    else:
        patient = PatientRegistrationForm()

    context = {
        'header' : 'Register as a patient',
        'form' : patient
    }

    return render(request, 'main_app/register.html', context)

def login_institution(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = email, password = password)
        if user:
            login(request, user)
            return redirect('frontend-index')
        else:
            messages.error(request, f'Incorrect email or password')
            return redirect('accounts-login-institution')
    else:
        form = AuthenticationForm()

    context = {
        'form' : form
    }

    return render(request, 'main_app/login.html', context)

def register_institution(request):
    if request.method == 'POST':
        form = InstitutionRegistrationForm(request.POST)
        if form.is_valid():
            user = User(username = form.instance.email, is_patient = True, name = form.instance.institution_name)
            user.save()
            form.instance.user = user
            form.instance.save()
            form.save()
            messages.success(request, f'Account created! You may now log in.')
            return redirect('accounts-login-institution')
    else:
        patient = InstitutionRegistrationForm()

    context = {
        'header' : 'Register as an institution',
        'form' : patient
    }

    return render(request, 'main_app/register.html', context)

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PatientListCreate(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class InstitutionListCreate(generics.ListCreateAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer

class InstitutionGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer