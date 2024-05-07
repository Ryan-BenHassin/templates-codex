import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

class EmailHandler:
 def __init__(self, email_from, email_password, smtp_server, smtp_port):
 self.email_from = email_from
 self.email_password = email_password
 self.smtp_server = smtp_server
 self.smtp_port = smtp_port

 def send_email(self, subject, message, email_to, files=None):
 msg = EmailMessage()
 msg.set_content(message)
 msg['Subject'] = subject
 msg['From'] = self.email_from
 msg['Date'] = formatdate(localtime=True)
 msg['To'] = email_to

 if files:
 msg_p = MIMEMultipart()
 msg_p.attach(MIMEText(message, 'plain'))
 for f in files:
 with open(f, 'rb') as fp:
 msg_p.attach(MIMEApplication(fp.read(), Name=os.path.basename(f)))
 msg_p['Subject'] = subject
 msg_p['From'] = self.email_from
 msg_p['Date'] = formatdate(localtime=True)
 msg_p['To'] = email_to
 server = smtplib.SMTP(self.smtp_server, self.smtp_port)
 server.starttls()
 server.login(self.email_from, self.email_password)
 server.send_message(msg_p)
 server.quit()
 else:
 server = smtplib.SMTP(self.smtp_server, self.smtp_port)
 server.starttls()
 server.login(self.email_from, self.email_password)
 server.send_message(msg)
 server.quit()

# Usage:
email_handler = EmailHandler('your_email@gmail.com', 'your_password', 'smtp.gmail.com', 587)
email_handler.send_email('Test Email', 'This is a test email', 'recipient@example.com', ['file1.txt', 'file2.txt'])
