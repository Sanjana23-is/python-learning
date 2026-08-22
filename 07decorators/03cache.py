# Q3. Implement a decorator that caches the return value of a function, so that when it is called with the same arguments, the cached value is returned instead of re-executing the function.
import time

def cache(func):
    cache_value = {}
    def wrapper(*args):
        result = func(*args)
        
        return result
    return wrapper


def long_running_function(a, b):
    time.sleep(4)  # Simulate a long-running operation
    return a + b