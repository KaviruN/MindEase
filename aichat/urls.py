from django.urls import path, include
from . import views

app_name = 'aichat'

urlpatterns = [
    path('chat/', views.chat_view, name='chat'),
    path('get-chat-data/', views.get_chat_data, name='get_chat_data'),
]
