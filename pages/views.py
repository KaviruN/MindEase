from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from datetime import datetime
import time
from django.http import JsonResponse

# Create your views here.

def user_profile(request):
    if not request.user.is_authenticated:
        return redirect('user_auth:sign_in') 
    else:
        username = request.user
        user = User.objects.filter(username=username).first()
        profile = user.userprofile
        age = datetime.now().year - profile.birthday.year
        print(age)
        return render(request, 'profile.html', {'user':user, 'profile':profile, 'age':age})
    

def home(request):
    return render(request, 'home.html')
