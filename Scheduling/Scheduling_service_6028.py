import schedule
import time
from datetime import datetime

def job(message):
 print(f"{datetime.now()}: {message}")

def scheduler(api_key, schedule_time, message):
 schedule.every().day.at(schedule_time).do(job, message) # schedule task to run at specified time daily

 while True:
 schedule.run_pending()
 time.sleep(1)

# replace with your api key
api_key = "YOUR_API_KEY"

# replace with your schedule time in 24-hour format (HH:MM)
schedule_time = "10:30"

# replace with your message
message = " Scheduled task executed successfully"

scheduler(api_key, schedule_time, message)
