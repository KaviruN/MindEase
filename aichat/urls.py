from django.urls import path, include
from . import views

app_name = 'aichat'

urlpatterns = [
    path('chat/', views.chat, name='chat'),
]
