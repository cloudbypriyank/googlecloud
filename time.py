import time
import logging

logging.basicConfig(level=logging.INFO)

def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"{func.__name__} executed in {execution_time:.4f} seconds")
        return result
    return wrapper

@execution_time_decorator
def computationally_expensive_task():
    # Example of a computationally expensive task
    result = sum([i**2 for i in range(1000000)])
    return result
