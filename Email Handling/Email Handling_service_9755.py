import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, message, from_addr, password, to_addr):
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    body = message
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_addr, password)
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()

# usage
subject = 'Test Email'
message = 'This is a test email.'
from_addr = 'your-email@gmail.com'
password = 'your-password'
to_addr = 'receiver-email@gmail.com'

send_email(subject, message, from_addr, password, to_addr)