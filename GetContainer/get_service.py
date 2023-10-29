from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from data import check_and_trigger_alerts


def setup_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.start()

    # Schedule the job to check for due reminders and trigger alerts every minute
    scheduler.add_job(
        check_and_trigger_alerts,
        trigger=CronTrigger(second='0'),  # Runs every minute
        id='check_due_reminders',
        replace_existing=True
    )
