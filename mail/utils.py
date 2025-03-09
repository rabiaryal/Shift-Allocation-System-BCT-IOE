from django.core.mail import EmailMessage
from .models import Recipient
import os

def send_mail_with_attachment(subject, message, file_path):
    # Fetch all email addresses from the database
    # recipient_list = list(Recipient.objects.values_list('email', flat=True))
    example = [
        "sumeshdhoju@gmail.com",
        "foradditional00@gmail.com"
        
    ]
    recipient_list = example


    # Create email message
    email = EmailMessage(
        subject=subject,
        body=message,
        from_email="sumesh10.d@gmail.com",
        to=recipient_list,
    )

    # Attach file
    if file_path and os.path.exists(file_path):
            email.attach_file(file_path)
    else:
            raise FileNotFoundError(f"File not found: {file_path}")

    # Send email
    email.send()
    print("Email sent successfully!")
   
