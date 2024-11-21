from django.shortcuts import render
from django.contrib.auth.models import User
from datetime import datetime

# Create your views here.

def user_profile(request):
    if not User.is_authenticated:
        pass
    else:
        username = request.user
        user = User.objects.filter(username=username).first()
        profile = user.userprofile
        age = datetime.now().year - profile.birthday.year
        print(age)
        return render(request, 'profile.html', {'user':user, 'profile':profile, 'age':age})
