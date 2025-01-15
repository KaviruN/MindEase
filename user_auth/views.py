from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from datetime import datetime
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import random
from .forms import SignUpForm
from django.contrib.auth.models import User

def send_verification_email(user_email, username):
    verification_code = random.randint(100000, 999999)  # Generate a 6-digit random number
    subject = 'Your Verification Code'
    template_name = 'email_template.html'
    context = {
        'username': username,
        'verification_code': verification_code
    }
    convert_to_html_content =  render_to_string(
            template_name=template_name,
            context=context
    )
    plain_message = strip_tags(convert_to_html_content)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    try:
        send_mail(
        subject=subject,
        message=plain_message,
        from_email=email_from,
        recipient_list=recipient_list ,  # recipient_list is self explainatory
        html_message=convert_to_html_content  # Optional
    )
        print(f'email send done - {username}')
    except:
        print(f'email send fail - {username}')
    
    return verification_code

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate account until it is verified
            user.save()
            user.refresh_from_db()
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()
            
            # Send verification email
            verification_code = send_verification_email(user.email, user.username)
            request.session['verification_code'] = verification_code
            request.session['user_id'] = user.id
            
            return redirect('user_auth:verify')  # Redirect to verification page
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

def verify_code_view(request):
    if request.user.is_active:
        return redirect('user_auth:sign_in')
    else:
        if request.method == 'POST':
            entered_code = str(request.POST['code1']) + str(request.POST['code2']) + str(request.POST['code3']) + str(request.POST['code4']) + str(request.POST['code5']) + str(request.POST['code6'])
            if entered_code == str(request.session.get('verification_code')):
                user_id = request.session.get('user_id')
                user = User.objects.get(id=user_id)
                user.is_active = True
                user.save()
                return redirect('user_auth:sign_in')
            else:
                return HttpResponse('Invalid verification code.')
    return render(request, 'verify.html')

def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('pages:home')
            else:
                form.add_error(None, 'Invalid username or password')
        else:
            form.add_error(None, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'sign_in.html', {'form': form})

def sign_out(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, 'sign_out.html')
    else:
        return redirect('user_auth:sign_in')