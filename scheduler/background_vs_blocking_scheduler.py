"""
POC Objective:
Demonstrate the difference between BackgroundScheduler and BlockingScheduler
in APScheduler:
1. BackgroundScheduler runs jobs in the background, allowing main thread tasks to run concurrently.
2. BlockingScheduler blocks the main thread while scheduling jobs.
3. Shows effect of max_instances=1 to prevent overlapping jobs.

Requirements:
    apscheduler>=3.10.0
"""

import logging
import time
import threading
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
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
    Function that simulates a task running on the main thread.
    """
    logging.info(f"Blocking function started on thread: {threading.current_thread().name}")
    for i in range(5):
        logging.info(f"Working... {i+1}/5")
        time.sleep(2)
    logging.info("Blocking function finished!")


# -------------------------
# Main Execution
# -------------------------
def run_background_scheduler():
    logging.info("===== BackgroundScheduler Demo =====")
    scheduler = BackgroundScheduler()
    cron_trigger = CronTrigger(second="*/2")  # run every 2 seconds
    scheduler.add_job(my_job, cron_trigger, max_instances=1)
    scheduler.start()  # non-blocking
    logging.info("BackgroundScheduler started. Main thread remains free.")
    # Main thread task runs concurrently
    blocking_function()
    # Shutdown scheduler after main thread finishes
    scheduler.shutdown()
    logging.info("BackgroundScheduler stopped.")


def run_blocking_scheduler():
    logging.info("===== BlockingScheduler Demo =====")
    scheduler = BlockingScheduler()
    cron_trigger = CronTrigger(second="*/2")
    scheduler.add_job(my_job, cron_trigger, max_instances=1)
    logging.info("BlockingScheduler starting. Main thread blocked for scheduler.")
    scheduler.start()  # blocks main thread until Ctrl+C or shutdown
    blocking_function() ## this will never run as scheduler will block main thread and stop only when CTRL+C is pressed
    logging.info("BlockingScheduler stopped.")


if __name__ == "__main__":
    logging.info(f"Main thread: {threading.current_thread().name}")

    # Run BackgroundScheduler
    # run_background_scheduler()

    # Run BlockingScheduler
    run_blocking_scheduler()

    logging.info(f"Main thread after demos: {threading.current_thread().name}")
