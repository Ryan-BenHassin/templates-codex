import schedule
import time
import datetime

def job(message):
    print(f"Job executed at {datetime.datetime.now()} - {message}")

def setup_schedules():
    schedule.every(10).minutes.do(job, message='10 minutes job')
    schedule.every().hour.do(job, message='hourly job')
    schedule.every().day.at("10:30").do(job, message='daily job')
    schedule.every(5).to(6).minutes.do(job, message='5 to 6 minutes job')
    schedule.every(1).minutes.do(job, message='1 minute job')

def run_schedules():
    setup_schedules()
    while True:
      schedule.run_pending()
      time.sleep(1)

if __name__ == "__main__":
    run_schedules() 
