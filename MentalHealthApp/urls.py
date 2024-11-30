from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_auth.urls')),
    path('', include('pages.urls')),
    path('', include('modetracker.urls')),
    path('', include('aichat.urls')),
]
