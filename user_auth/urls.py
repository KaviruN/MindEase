from django.urls import path, include
from .views import sign_up, sign_in

app_name = 'user_auth'

urlpatterns = [
   path('signup/', sign_up, name="sign_up"),# Include the auth app's URLs
   path('signin/', sign_in, name="sign_in"),# Include the auth app's URLs
]
