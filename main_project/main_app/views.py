from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import User, Patient, Institution
from django.contrib.auth.forms import AuthenticationForm
from .forms import PatientRegistrationForm, InstitutionRegistrationForm
from .serializers import UserSerializer, PatientSerializer, InstitutionSerializer
from rest_framework import generics
import qrcode
from datetime import date
import random
from itertools import chain

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def home(request):
    return render(request, 'main_app/home.html')

def login_patient(request):
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
            return redirect('accounts-login-patient')
    else:
        form = AuthenticationForm()

    context = {
        'header' : 'Login as a patient',
        'form' : form
    }

    return render(request, 'main_app/login.html', context)

def register_patient(request):
    patient = PatientRegistrationForm()
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username = form.cleaned_data['email'], password = form.cleaned_data['password1'])
            user.is_patient = True
            user.name = form.instance.first_name
            user.save()
            form.instance.user = user
            form.instance.age = calculate_age(form.cleaned_data['date_of_birth'])
            form.instance.uhc = bool(random.getrandbits(1))
            patient = form.save()
            messages.success(request, f'Account created! You may now log in.')
            return redirect('accounts-login-patient')

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
        'header' : 'Login as an institution',
        'form' : form
    }

    return render(request, 'main_app/login.html', context)

def register_institution(request):
    institution = InstitutionRegistrationForm()
    if request.method == 'POST':
        form = InstitutionRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username = form.instance.email, password = form.cleaned_data['password1'])
            user.is_institution = True
            user.name = form.instance.institution_name
            user.save()
            form.instance.user = user
            institution = form.save()
            messages.success(request, f'Account created! You may now log in.')
            return redirect('accounts-login-patient')

    context = {
        'header' : 'Register as an institution',
        'form' : institution
    }

    return render(request, 'main_app/register.html', context)

def qrcodepage(request):
    patient = Patient.objects.filter(user_id = request.user.id).first()
    if patient:
        data = 'http://localhost:8000/api/patients/' + str(patient.id) + '/'
        qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
        qr.add_data(data)
        qr.make(fit = True)
        img = qr.make_image(fill = 'black', back_color = 'white')
        img.save('main_app/static/main_app/qrcode.png')
        return render(request, 'main_app/qrcode.html')
    return redirect('frontend-index')

def queue(request):
    institution = Institution.objects.filter(user_id = request.user.id).first()
    if institution or True:
        patients = Patient.objects.all()
        patients_old = patients.filter(age__gt = 60)
        patients_young = patients.filter(age__lte = 60)
        patients_young_uhc = patients_young.filter(uhc = True)
        patients_young = patients_young.filter(uhc = False)
        patients = list(chain(patients_old, patients_young_uhc, patients_young))

        context = {
            'patients' : patients,
        }
        return render(request, 'main_app/queue.html', context)
    return redirect('frontend-index')

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