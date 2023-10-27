import logging
from get_service import setup_scheduler

logging.basicConfig(filename='logger.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(threadName)-10s %('
                                                                      'message)s', )

if __name__ == "__main__":
    try:
        setup_scheduler()
    except KeyboardInterrupt:
        pass
    finally:
        logging.info("Shutting down scheduler")
        setup_scheduler.shutdown()
