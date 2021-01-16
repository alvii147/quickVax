from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListCreate.as_view(), name = 'api-users-list-create'),
    path('users/<int:pk>/', views.UserGetUpdateDelete.as_view(), name = 'api-users-get-update-delete'),
]
