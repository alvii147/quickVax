from django import forms
from django.contrib.auth.models import User
from .models import Patient, Institution
from django.contrib.auth.forms import UserCreationForm

class DateInput(forms.DateInput):
    input_type = 'date'

class PatientRegistrationForm(UserCreationForm):
    date_of_birth = forms.DateField(widget = DateInput)
    class Meta:
        model = Patient
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name', 'middle_initial', 'date_of_birth', 'address_line_1', 'address_line_2', 'city', 'province', 'postal_code']

class InstitutionRegistrationForm(UserCreationForm):
    class Meta:
        model = Institution
        fields = ['email', 'password1', 'password2', 'institution_name', 'license', 'address_line_1', 'address_line_2', 'city', 'province', 'postal_code']