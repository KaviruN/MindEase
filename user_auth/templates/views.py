from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import random

def send_verification_email(user_email):
    verification_code = random.randint(100000, 999999)  # Generate a 6-digit random number
    subject = 'Your Verification Code'
    message = f'Your verification code is {verification_code}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    send_mail(subject, message, email_from, recipient_list)
    
    return verification_code


def send_verification_email_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        verification_code = send_verification_email(email)
        request.session['verification_code'] = verification_code
        return HttpResponse('Verification email sent!')
    return render(request, 'index.html')

def verify_code_view(request):
    if request.method == 'POST':
        entered_code = request.POST['verification_code']
        if entered_code == str(request.session.get('verification_code')):
            return HttpResponse('Email verified successfully!')
        else:
            return HttpResponse('Invalid verification code.')
    return render(request, '2.html')