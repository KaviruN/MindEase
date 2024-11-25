from django.urls import path, include
from .views import sign_up, sign_in, sign_out, verify_code_view

app_name = 'user_auth'

urlpatterns = [
   path('signup/', sign_up, name="sign_up"),# Include the auth app's URLs
   path('signin/', sign_in, name="sign_in"),# Include the auth app's URLs
   path('signout/', sign_out, name="sign_out"),# Include the auth app's URLs
   path('f/', verify_code_view, name="verify"),# Include the auth app's URLs
]
