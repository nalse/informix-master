from django.core.mail import send_mail
from django.conf import settings
import uuid

def send_forget_password_mail(email, token):
    subject ='your forget password link'
    message = f'Hi, mnasgdjsagdj http://127.0.0.0:8000/forget-password/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list =[email]
    send_mail(subject,message,email_from,recipient_list)
    return True