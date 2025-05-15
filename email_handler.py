import smtplib
from email.message import EmailMessage

SENDER_EMAIL = "your_email@example.com"
SENDER_PASSWORD = "your_app_password"  # Use App Password if using Gmail

def send_email(to, subject, content):
    msg = EmailMessage()
    msg.set_content(content)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = to

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
        smtp.send_message(msg)
