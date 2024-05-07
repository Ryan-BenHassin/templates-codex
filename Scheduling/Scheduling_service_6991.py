# TODO
import schedule
import time
import datetime

def job(message):
    print(f"Current time: {datetime.datetime.now()}")
    print(message)

def scheduler():
    schedule.every(10).minutes.do(job, message='Good morning!')
    schedule.every().hour.do(job, message='It\'s time for lunch!')
    schedule.every().day.at("10:30").do(job, message='Have a good day!')
    schedule.every().monday.do(job, message='Happy Monday!')
    schedule.every().wednesday.at("13:15").do(job, message='Happy Hump Day!')
    schedule.every().minute.at(":17").do(job, message='Time for a break!')

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    scheduler()