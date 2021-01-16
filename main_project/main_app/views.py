from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Patient
from .forms import PatientRegistrationForm
from .serializers import PatientSerializer
from rest_framework import generics

def home(request):
    return render(request, 'main_app/home.html')

def register_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created! You may now log in.')
            return redirect('accounts-login')
    else:
        form = PatientRegistrationForm()

    context = {
        'header' : "Register as a patient",
        'form' : form
    }

    return render(request, 'main_app/register.html', context)

class PatientListCreate(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer