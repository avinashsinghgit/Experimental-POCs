"""
Here, all code runs in the main thread. 
Jobs and the main async task run concurrently on the same asyncio event loop using async/await.
************  Concurrency is achieved via coroutine switching, not via multiple event loops or threads.   ************
Even with multiple scheduled jobs, all jobs execute on the same main thread and share the same event loop.
"""

import asyncio
import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(threadName)s | %(message)s"
)

# -------------------------
# Async job definition
# -------------------------
async def async_job():
    logging.info("Async job started...")
    await asyncio.sleep(5)
    logging.info("Async job finished!")

# -------------------------
# Main async task
# -------------------------
async def main_async_task():
    for i in range(5):
        logging.info(f"Main async task working... {i+1}/5")
        await asyncio.sleep(5)
    logging.info("Main async task finished!")

async def secondary_job():
    for i in range(5):
        logging.info(f"Secondary async task working... {5*(i+1)}")
        await asyncio.sleep(5)
    logging.info("Secondary async task finished!")



# -------------------------
# Main execution
# -------------------------
async def main():
    logging.info("Starting AsyncIOScheduler demo")
    
    scheduler = AsyncIOScheduler()
    
    cron_trigger = CronTrigger(second="*/2")
    scheduler.add_job(async_job, cron_trigger, max_instances=2)
    scheduler.add_job(secondary_job, cron_trigger, max_instances=2)
    
    scheduler.start()  
    await main_async_task()
    scheduler.shutdown()
    logging.info("AsyncIOScheduler demo finished")

# Run the async main
asyncio.run(main())
