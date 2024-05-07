import functools
class Cache:
 cache = {}

 def __init__(self, ttl=60): # 1 minute default TTL
 self.ttl = ttl

 def set(self, key, value):
 self.cache[key] = {'value': value, 'ttl': self.ttl, 'timestamp': time.time()}

 def get(self, key):
 if key in self.cache:
 cache_item = self.cache[key]
 if cache_item['ttl'] + cache_item['timestamp'] > time.time():
 return cache_item['value']
 else:
 del self.cache[key]
 return None

 def delete(self, key):
 if key in self.cache:
 del self.cache[key]

def cache_decorator(ttl=60):
 cache = Cache(ttl)

 def decorator(func):
 @functools.wraps(func)
 def wrapper(*args, **kwargs):
 cache_key = repr((args, kwargs))
 cached_value = cache.get(cache_key)
 if cached_value is not None:
 return cached_value
 value = func(*args, **kwargs)
 cache.set(cache_key, value)
 return value
 return wrapper
 return decorator
