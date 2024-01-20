import os
import smtplib
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

from dotenv import load_dotenv

DOTENV_PATH = Path(__file__).parent / 'static' / '.env'
HTML_PATH = Path(__file__).parent / 'static' / 'class_303.html'

load_dotenv(DOTENV_PATH)

# Sender and Recipient Data
sender = os.getenv('FROM_EMAIL')

recipient = sender

# SMTP Configurations
smtp_server = os.getenv('GOOGLE_SMTP')
smtp_port = int(os.getenv('GOOGLE_SMTP_PORT'))
smtp_username = sender
smtp_password = os.getenv('EMAIL_PASSWORD')

# Text message
with open(HTML_PATH, 'r') as file_:
    text_file = file_.read()
    template = string.Template(text_file)
    text_email = template.substitute(name='John', sender='Mary')
    print(text_email)

# Convert the text message into MIMEMultiPart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = sender
mime_multipart['to'] = recipient
mime_multipart['subject'] = 'This is the subject of the email'

# _subtype could be 'plain' for test, but it will be used 'html'
email_body = MIMEText(text_email, 'html', )
mime_multipart.attach(email_body)

# Send e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('E-mail sent with success')

