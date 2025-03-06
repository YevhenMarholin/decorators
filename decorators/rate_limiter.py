import time
from collections import deque
from functools import wraps

def rate_limiter(calls_per_minute):
    interval = 60 / calls_per_minute
    calls = deque()

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            while calls and current_time - calls[0] > 60:
                calls.popleft()

            if len(calls) >= calls_per_minute:
                raise ValueError("Rate limit exceeded. Try again later.")

            calls.append(current_time)
            return func(*args, **kwargs)
        return wrapper
    return decorator
