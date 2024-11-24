from django.urls import path, include
from . import views

app_name = 'pages'

urlpatterns = [
    path('profile/',views.user_profile, name='profile'),
    path('',views.home, name='home'),
    path('contact/',views.contact, name='contact'),
]

