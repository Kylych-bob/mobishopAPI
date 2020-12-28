from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

#SEND MESSAGE

def send_confirmation_email(user):
    context = {
        "email": user.email,
        "doamin": "http:localhost:8000/",
        "activation_code": user.activation_code,
        "text_detail": "Thank you for register",
    }
    msg_html = render_to_string("email.html", context)
    plain_message = strip_tags(msg_html)
    subject = "Activation Account"
    to_emails = user.email
    mail.send_mail(
        subject,
        plain_message,
        "tteest624@gmail.com",
        [to_emails, ],
        html_message = msg_html
    )

    
   