from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import User, Patient, Institution
from django.contrib.auth.forms import AuthenticationForm
from .forms import PatientRegistrationForm, InstitutionRegistrationForm
from .serializers import UserSerializer, PatientSerializer, InstitutionSerializer
from rest_framework import generics
import qrcode

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
        data = 'https://localhost:8000/api/patient/' + str(patient.id)
        print(data)
        qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
        qr.add_data(data)
        qr.make(fit = True)
        img = qr.make_image(fill = 'black', back_color = 'white')
        img.save('main_app/static/main_app/qrcode.png')
        return render(request, 'main_app/qrcode.html')
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