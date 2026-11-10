import logging
import time
# Configure logging for debugging code execution
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
def profiled_task_execution():
    start_time = time.perf_counter()   
    logging.info("Starting data processing pipeline...")
    # Simulated processing work
    time.sleep(0.1)    
    end_time = time.perf_counter()
    logging.info(f"Task completed in {end_time - start_time:.4f} seconds.")
profiled_task_execution()