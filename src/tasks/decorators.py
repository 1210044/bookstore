import time, signal
from datetime import timedelta
from django.core.cache import cache


def raise_timeout(signum, frame):
    raise TimeoutError("Function execution exceeded the maximum allowed time")


def single(max_processing_time: timedelta):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if cache.get(func.__name__):
                return None
            
            cache.set(func.__name__, 'lock', timeout=max_processing_time.seconds + 1)
            signal.signal(signal.SIGALRM, raise_timeout)
            signal.alarm(max_processing_time.seconds)

            try:
                result = func(*args, **kwargs)
            except TimeoutError as e:
                print(e)
                return
            finally:
                signal.alarm(0)
                cache.delete(func.__name__)
            
            return result
        return wrapper
    return decorator


@single(max_processing_time=timedelta(minutes=2))
def process_transaction():
    time.sleep(2)