from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('frontend.urls')),
    path('app/', include('main_app.app_urls')),
    path('accounts/', include('main_app.accounts_urls')),
    path('api/', include('main_app.api_urls')),
    path('admin/', admin.site.urls),
]
