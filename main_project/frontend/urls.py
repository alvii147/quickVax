from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name = 'frontend-index'),
    path('queue/', views.index, name = 'frontend-queue'),
    path('how/', views.index, name = 'frontend-how'),
    path('faq/', views.index, name = 'frontend-faq')
]
