import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from data import check_and_trigger_alerts

# Initialize the scheduler
scheduler = BackgroundScheduler()
scheduler.start()
logging.basicConfig(filename='logger.log', encoding='utf-8', level=logging.DEBUG, filemode='w')


def app():
    scheduler.add_job(
        check_and_trigger_alerts,
        trigger=CronTrigger(second='0'),  # Runs every minute
        id='check_due_reminders',
        replace_existing=True
    )


if __name__ == "__main__":
    try:
        app()
    except KeyboardInterrupt:
        exit(0)
    finally:
        # Shut down the scheduler gracefully on program exit
        scheduler.shutdown()
