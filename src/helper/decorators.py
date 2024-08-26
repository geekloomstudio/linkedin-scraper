import functools
import logging
import random
import time
from datetime import datetime


def sleep(start_time=None, end_time=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if end_time:
                sleep_time = random.randint(start_time, end_time)  # nosec
            else:
                sleep_time = start_time
            time.sleep(sleep_time)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def timer(func):
    def wraper():
        start_time = datetime.now()
        result = func()
        end_time = datetime.now()
        logging.info("start_time: %s", repr(start_time))
        logging.info("end_time: %s", repr(end_time))
        logging.info("duration: %s", repr((end_time - start_time).seconds))
        return result

    return wraper
