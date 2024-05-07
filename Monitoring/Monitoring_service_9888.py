import os
import time
import psutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_size(bytes, suffix="B"):
 factor = 1024
 for unit in ["", "K", "M", "G", "T", "P"]:
 if bytes < factor:
 return f"{bytes:.2f}{unit}{suffix}"
 bytes /= factor

def cpu_usage():
 return str(psutil.cpu_percent()) + "%"

def memory_usage():
 svmem = psutil.virtual_memory()
 return f"Total: {get_size(svmem.total)}, Available: {get_size(svmem.available)}, Used: {get_size(svmem.used)}, Percentage: {svmem.percent}%"

def disk_usage():
 partition_usage = psutil.disk_usage("/")
 return f"Total: {get_size(partition_usage.total)}, Used: {get_size(partition_usage.used)}, Free: {get_size(partition_usage.free)}, Percentage: {partition_usage.percent}%"

def network_usage():
 net_io = psutil.net_io_counters()
 return f"Bytes Sent: {get_size(net_io.bytes_sent)}, Bytes Received: {get_size(net_io.bytes_recv)}"

def send_email(subject, message, from_addr, to_addr, smtp_server, smtp_port, smtp_user, smtp_pass):
 msg = MIMEMultipart()
 msg['From'] = from_addr
 msg['To'] = to_addr
 msg['Subject'] = subject

 body = message
 msg.attach(MIMEText(body, 'plain'))

 server = smtplib.SMTP_SSL(smtp_server, smtp_port)
 server.login(smtp_user, smtp_pass)
 text = msg.as_string()
 server.sendmail(from_addr, to_addr, text)
 server.quit()

def monitor_system():
 cpu_usage_info = cpu_usage()
 memory_usage_info = memory_usage()
 disk_usage_info = disk_usage()
 network_usage_info = network_usage()

 message = f"CPU Usage: {cpu_usage_info}\nMemory Usage: {memory_usage_info}\nDisk Usage: {disk_usage_info}\nNetwork Usage: {network_usage_info}"
 subject = "System Monitoring Report"

 send_email(subject, message, "your_email@gmail.com", "recipient_email@gmail.com", "smtp.gmail.com", 465, "your_email@gmail.com", "your_password")

while True:
 monitor_system()
 time.sleep(60)
