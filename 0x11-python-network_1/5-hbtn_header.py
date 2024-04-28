#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays 
the value of the variable X-Request-Id in the response header
"""

import sys
import requests

url = sys.argv[1] if len(sys.argv) > 1 else ''
if not url:
    exit(1)

res = requests.get(url)
req_id = res.headers["X-Request-Id"]
print(req_id)
