from django import forms
from django.contrib.auth.models import User
from .models import Patient
from django.contrib.auth.forms import UserCreationForm
"""
class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label = 'First Name', required = True, help_text = 'Enter first name', widget = forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'eg. Wade'}))
    last_name = forms.CharField(label = 'Last Name', required = True, help_text = 'Enter last name', widget = forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'eg. Wilson'}))
    middle_name = forms.CharField(label = 'Middle Name', required = True, help_text = 'Enter middle name', widget = forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'eg. Some'}))
    email = forms.EmailField(label = 'Email', required = True, help_text = 'Enter email address', widget = forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'eg. wwilson@xforce.com'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'middle_name', 'email', 'password1', 'password2']
        widgets = {
            'username' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'eg. wwilson1991'}),
        }"""

class DateInput(forms.DateInput):
    input_type = 'date'

class PatientRegistrationForm(UserCreationForm):
    date_of_birth = forms.DateField(widget = DateInput)
    class Meta:
        model = Patient
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name', 'middle_initial', 'date_of_birth', 'address_line_1', 'address_line_2', 'city', 'province', 'postal_code']