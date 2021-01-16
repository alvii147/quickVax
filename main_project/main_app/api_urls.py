from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.PatientListCreate.as_view(), name = 'api-patient-list-create'),
    path('patients/<int:pk>/', views.PatientGetUpdateDelete.as_view(), name = 'api-patient-get-update-delete'),
]