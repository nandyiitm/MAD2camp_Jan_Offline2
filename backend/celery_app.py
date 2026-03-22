from celery import Celery
from celery.schedules import crontab

app = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
)

app.conf.update(
    timezone='Asia/Kolkata',
    enable_utc=False,
)

import time
from datetime import timedelta
from app import app as flask_app
from models import User
from mail import send_email

@app.task()
def send_daily_reminders():
    print("Sending daily reminders...")
    with flask_app.app_context():
        users = User.query.all()
        for user in users:
            time.sleep(1)  # Simulate delay
            send_email(
                to_email=user.email,
                subject="Daily Reminder",
                body="This is your daily reminder to check latest mobiles!"
            )
            print(f"Reminder sent to {user.email}")
    return "Daily reminders sent successfully!"

@app.task()
def send_report(user_email):
    print(f"Generating report for {user_email}...")
    time.sleep(30)  # Simulate report generation
    send_email(
        to_email=user_email,
        subject="Your Report is Ready",
        body="Your requested report has been generated. Please check your dashboard for details.",
        report_url="http://localhost:5000/static/reports/1_report.csv"
    )
    print(f"Report sent to {user_email}")
    return f"Report sent to {user_email}"

app.conf.beat_schedule = {
    'send-daily-reminders-every-morning': {
        'task': 'celery_app.send_daily_reminders',
        'schedule': crontab(hour=15, minute=5),
        # 'schedule': timedelta(seconds=5),  # Every hour for testing
    },
}