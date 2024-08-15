#!/usr/bin/env python3
"""In this tasks, we will implement a get_page function
(prototype: def get_page(url: str) -> str:). The core of
the function is very simple. It uses the requests module
to obtain the HTML content of a particular URL and returns it.

Start in a new file named web.py and do not reuse the code
written in exercise.py.

Inside get_page track how many times a particular URL was
accessed in the key "count:{url}" and cache the result with
an expiration time of 10 seconds.

Tip: Use http://slowwly.robertomurray.co.uk to simulate
a slow response and test your caching."""

import redis
import requests
from functools import wraps

# Connect to Redis
r = redis.Redis()

def cache_and_count(url):
    """Decorator to handle caching and counting of URL accesses"""
    cache_key = "cached:" + url
    count_key = "count:" + url
    
    # Check if the response is cached
    cached_value = r.get(cache_key)
    if cached_value:
        print("Cache hit")
        return cached_value.decode("utf-8")
    
    # Fetch new content if not cached or expired
    print("Cache miss")
    response = requests.get(url)
    html_content = response.text
    
    # Update the cache and set expiration
    r.setex(cache_key, 10, html_content)
    
    # Increment the access count
    r.incr(count_key)
    
    return html_content

@cache_and_count
def get_page(url: str) -> str:
    """Obtain the HTML content of a particular URL"""
    return cache_and_count(url)

if __name__ == "__main__":
    # Test the function
    print(get_page('http://slowwly.robertomurray.co.uk'))

