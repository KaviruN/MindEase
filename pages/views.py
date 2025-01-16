from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from datetime import datetime
import time
from django.core.mail import send_mail
from django.conf import settings


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
    context = {}
    if request.user.is_authenticated:
        user = User.objects.filter(username=request.user).first()
        context = {'user':user}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')


def contact(request):
    context = {}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['meassage']
        subject = 'Contact Form Submission'
        message = f'Name: {name}\nEmail: {email}\n\n{message}'

        if name and email and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, ['mindeaseorg@gmail.com'])
                context['result'] = 'Message sent successfully'
            except Exception as e:
                context['result'] = f'Error sending message: {e}'
        else:
            context['result'] = 'All fields are required'
        
    return render(request, 'contact.html', context)
