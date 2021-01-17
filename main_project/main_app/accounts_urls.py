from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/patient', views.register_patient, name = 'accounts-register-patient'),
    path('login/patient', views.login_patient, name = 'accounts-login-patient'),
    path('register/institution', views.register_institution, name = 'accounts-register-institution'),
    path('login/institution', views.login_institution, name = 'accounts-login-institution'),
    #path('logout/', auth_views.LogoutView.as_view(template_name = 'main_app/logout.html'), name = 'accounts-logout'),
]
