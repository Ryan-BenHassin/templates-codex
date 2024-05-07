import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

class EmailHandler:
    def __init__(self, sender_email, password, smtp_server, smtp_port):
        self.sender_email = sender_email
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, receiver_email, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        body = message
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(self.sender_email, self.password)
        text = msg.as_string()
        server.sendmail(self.sender_email, receiver_email, text)
        server.quit()

email_handler = EmailHandler('your_email@gmail.com', 'your_password', 'smtp.gmail.com', 587)
email_handler.send_email('receiver_email@example.com', 'Test Email', 'This is a test email')