from django.urls import path, include
from .views import sign_up

urlpatterns = [
   path('', sign_up),# Include the auth app's URLs
]
