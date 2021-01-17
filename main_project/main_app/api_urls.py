from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListCreate.as_view(), name = 'api-users-list-create'),
    path('users/<int:pk>/', views.UserGetUpdateDelete.as_view(), name = 'api-users-get-update-delete'),
    path('patients/', views.PatientListCreate.as_view(), name = 'api-patient-list-create'),
    path('patients/<int:pk>/', views.PatientGetUpdateDelete.as_view(), name = 'api-patient-get-update-delete'),
    path('institutions/', views.PatientListCreate.as_view(), name = 'api-institution-list-create'),
    path('institutions/<int:pk>/', views.PatientGetUpdateDelete.as_view(), name = 'api-institution-get-update-delete'),
]