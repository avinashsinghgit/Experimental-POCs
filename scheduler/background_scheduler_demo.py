"""
POC Objective:
Demonstrate how BackgroundScheduler in APScheduler runs jobs in the background 
without blocking the main thread, allowing the main thread to execute other tasks.

requierments :-
    apscheduler>=3.10.0

"""

import logging
import time
import threading
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

# -------------------------
# Logging Configuration
# -------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(threadName)s | %(message)s"
)

# -------------------------
# Job Definitions
# -------------------------
def my_job():
    """
    Scheduled job that simulates a long-running task.
    """
    logging.info("Job started...")
    time.sleep(5)  # simulate long task
    logging.info("Job finished!")


def blocking_function():
    """
    Function that runs on the main thread to simulate blocking tasks.
    """
    logging.info(f"Blocking function started on thread: {threading.current_thread().name}")
    for i in range(5):
        logging.info(f"Working... {i+1}/5")
        time.sleep(2)
    logging.info("Blocking function finished!")

# -------------------------
# Main Execution
# -------------------------
if __name__ == "__main__":
    logging.info(f"Main thread before starting scheduler: {threading.current_thread().name}")

    # Initialize BackgroundScheduler
    scheduler = BackgroundScheduler()
    
    # Schedule `my_job` every 2 seconds
    cron_trigger = CronTrigger(second="*/2")
    scheduler.add_job(my_job, cron_trigger, max_instances=1)

    # Start the scheduler (does NOT block main thread)
    scheduler.start()
    logging.info("BackgroundScheduler started. Main thread remains free.")

    # Execute blocking function on main thread
    blocking_function()

    logging.info(f"Main thread after blocking: {threading.current_thread().name}")
