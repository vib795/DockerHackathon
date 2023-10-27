import logging
from get_service import setup_scheduler

logging.basicConfig(filename='logger.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(threadName)-10s %('
                                                                      'message)s', )

if __name__ == '__main__':
    scheduler = setup_scheduler()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Shutting down...")
        scheduler.shutdown()
