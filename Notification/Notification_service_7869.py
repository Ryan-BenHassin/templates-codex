#TODO
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_notification(recipient, subject, message, smtp_server, smtp_port, smtp_user, smtp_password):
 msg = MIMEMultipart()
 msg['From'] = smtp_user
 msg['To'] = recipient
 msg['Subject'] = subject
 body = message
 msg.attach(MIMEText(body, 'plain'))
 server = smtplib.SMTP(smtp_server, smtp_port)
 server.starttls()
 server.login(smtp_user, smtp_password)
 text = msg.as_string()
 server.sendmail(smtp_user, recipient, text)
 server.quit()

if __name__ == "__main__":
 recipient = "recipient@example.com"
 subject = "Test Notification"
 message = "This is a test notification"
 smtp_server = "smtp.example.com"
 smtp_port = 587
 smtp_user = "your-smtp-username"
 smtp_password = "your-smtp-password"
 send_notification(recipient, subject, message, smtp_server, smtp_port, smtp_user, smtp_password)
