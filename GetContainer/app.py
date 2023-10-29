import logging
from get_service import setup_scheduler
import threading

logging.basicConfig(filename='logger.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(threadName)-10s %(message)s')


def run_scheduler():
    scheduler = setup_scheduler()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Shutting down...")
        scheduler.shutdown()


if __name__ == '__main__':
    # Create a thread to run the scheduler
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.daemon = True  # Set the thread as a daemon so it exits when the main program exits

    # Start the scheduler thread
    scheduler_thread.start()

    # The main thread can continue with other tasks, or you can add additional code here as needed

    # You may want to add some form of wait or control mechanism for the main thread to interact with the scheduler if necessary
    # For example, you could implement a signal handler to gracefully shut down the scheduler.

    # For demonstration purposes, this main thread just waits for the scheduler thread to finish
    scheduler_thread.join()
