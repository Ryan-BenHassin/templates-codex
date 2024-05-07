#TODO
from functools import lru_cache

class CachingService:

    def __init__(self):
        self.cache = {}

    def fibonacci(self, n):
        @lru_cache(maxsize=256)
        def fib(n):
            if n < 2:
                return n
            return fib(n-1) + fib(n-2)
        return fib(n)

    def put(self, key, value):
        self.cache[key] = value

    def get(self, key):
        return self.cache.get(key)

    def invalidate(self, key):
        if key in self.cache:
            del self.cache[key]

caching_service = CachingService()