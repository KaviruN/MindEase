from django.urls import path, include
from .views import sign_up

app_name = 'user_auth'

urlpatterns = [
   path('singup/', sign_up, name="sign_up"),# Include the auth app's URLs
]
