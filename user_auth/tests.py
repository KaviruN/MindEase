from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import random

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.mail.yahoo.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'mind_ease@yahoo.com'
# EMAIL_HOST_PASSWORD = '5XE+)3V6.Wf&&]"'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'kaviruyt@gmail.com'
EMAIL_HOST_PASSWORD = 'zeuw pdrs obue ktjc'
username = 'kaviru'

# Create your tests here.
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
    email_from = EMAIL_HOST_USER
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


a = send_verification_email('mind_ease@yahoo.com', username)

print(a)