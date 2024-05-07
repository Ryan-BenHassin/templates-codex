# TODO
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_function(param):
    # Simulate an expensive operation
    result = param * 2  # Replace with your actual expensive operation
    return result

def main():
    print(expensive_function(5))  # Cache miss, result is computed
    print(expensive_function(5))  # Cache hit, result is retrieved from cache

if __name__ == "__main__":
    main()