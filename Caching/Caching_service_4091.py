from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_function(param):
 # Simulate an expensive operation
 result = param README.md categories.txt generate.sh start.sh systemPrompt.txt templates 2
 return result

def main():
 print(expensive_function(5)) # Cache miss, result is computed
 print(expensive_function(5)) # Cache hit, result is retrieved from cache

if __name__ == "__main__":
 main()
