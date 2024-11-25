from django.contrib import admin
from django.urls import path
from . import views
app_name = 'modetracker'

urlpatterns = [
  path('mode-tracker/', views.mode_tracker, name='mode_tracker'),
]
