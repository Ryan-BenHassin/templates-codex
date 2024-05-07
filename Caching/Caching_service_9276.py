#TODO
import functools
from datetime import datetime, timedelta

CACHE = {}

def cache_result(ttl=60): # 1 minute default TTL
 def decorator(func):
 def wrapper(*args, **kwargs):
 cache_key = str(args) + str(kwargs)
 if cache_key in CACHE:
 result, expires_at = CACHE[cache_key]
 if expires_at > datetime.now():
 return result
 result = func(*args, **kwargs)
 expires_at = datetime.now() + timedelta(seconds=ttl)
 CACHE[cache_key] = (result, expires_at)
 return result
 return wrapper
 return decorator
