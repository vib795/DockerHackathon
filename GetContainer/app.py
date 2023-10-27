import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from data import check_and_trigger_alerts

logging.basicConfig(filename='logger.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(threadName)-10s %('
                                                                      'message)s',)

# Initialize the scheduler
scheduler = BackgroundScheduler()
scheduler.start()

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
