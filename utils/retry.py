import time
import functools
import os

def retry(max_attempts=None, delay=None, exceptions=(Exception,)):
    """
    Retry decorator for flaky actions.
    Values can be overridden by Robot Framework variables:
      ${RETRY_ATTEMPTS}, ${RETRY_DELAY}
    """
    # Read from environment if not passed explicitly
    env_attempts = int(os.getenv("RETRY_ATTEMPTS", "3"))
    env_delay = int(os.getenv("RETRY_DELAY", "2"))

    max_attempts = max_attempts or env_attempts
    delay = delay or env_delay

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 1
            while attempt <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"[Retry] Attempt {attempt} failed: {e}")
                    if attempt == max_attempts:
                        raise
                    time.sleep(delay)
                    attempt += 1
        return wrapper
    return decorator
