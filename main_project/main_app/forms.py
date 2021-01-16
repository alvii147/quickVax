from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label = 'First Name', required = True, help_text = 'Enter first name', widget = forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'eg. Wade'}))
    last_name = forms.CharField(label = 'Last Name', required = True, help_text = 'Enter last name', widget = forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'eg. Wilson'}))
    email = forms.EmailField(label = 'Email', required = True, help_text = 'Enter email address', widget = forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'eg. wwilson@xforce.com'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'eg. wwilson1991'}),
        }
