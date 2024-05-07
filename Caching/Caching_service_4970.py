#TODO
from functools import lru_cache

class CachingService:

 def __init__(self):
 self.cache = {}

 @lru_cache(maxsize=256)
 def fibonacci(self, n):
 if n < 2:
 return n
 return self.fibonacci(n-1) + self.fibonacci(n-2)

 def put(self, key, value):
 self.cache[key] = value

 def get(self, key):
 return self.cache.get(key)

 def invalidate(self, key):
 if key in self.cache:
 del self.cache[key]

caching_service = CachingService()
