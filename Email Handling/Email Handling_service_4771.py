import smtplib
from email.message import EmailMessage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
import os

class EmailHandler:
    def __init__(self, email_from, email_password, smtp_server, smtp_port):
        self.email_from = email_from
        self.email_password = email_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, subject, message, email_to, files=None):
        # Ensure email_to is a list
        if not isinstance(email_to, list):
            email_to = [email_to]

        if files:
            msg = MIMEMultipart()
            msg.attach(MIMEText(message, 'plain'))
            for f in files:
                with open(f, 'rb') as fp:
                    part = MIMEApplication(fp.read(), Name=os.path.basename(f))
                    part['Content-Disposition'] = f'attachment; filename="{os.path.basename(f)}"'
                    msg.attach(part)
        else:
            msg = EmailMessage()
            msg.set_content(message)

        msg['Subject'] = subject
        msg['From'] = self.email_from
        msg['Date'] = formatdate(localtime=True)
        msg['To'] = ", ".join(email_to)  # Join all emails into a single string separated by commas

        # Connect to the server and send the email
        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(self.email_from, self.email_password)
        server.send_message(msg)
        server.quit()

# Usage example with multiple recipients:
email_handler = EmailHandler('sender-email@gmail.com', 'passwordt', 'smtp.gmail.com', 587)
email_handler.send_email(
    'Test Email', 
    'This is a test email', 
    ['recipient1@gmail.com', 'recipient2@gmail.com', 'recipient3@gmail.com'], 
    ['file1.txt']
)
