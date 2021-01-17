from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name = 'frontend-index'),
    path('qrcode', views.qrcodepage, name = 'qrcode'),
    path('queue', views.queue, name = 'queue'),
]
