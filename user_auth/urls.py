from django.urls import path, include
from .views import sign_up, sign_in, sign_out, verify_code_view

app_name = 'user_auth'

urlpatterns = [
   path('signup/', sign_up, name="sign_up"),
   path('signin/', sign_in, name="sign_in"),
   path('signout/', sign_out, name="sign_out"),
   path('verify/', verify_code_view, name="verify"),
]
