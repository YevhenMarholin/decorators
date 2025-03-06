from functools import lru_cache

def cache_results(func):
    cached_func = lru_cache(maxsize=None)(func)
    return cached_func
