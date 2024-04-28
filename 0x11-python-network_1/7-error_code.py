#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays 
the value of the variable X-Request-Id in the response header
"""
import sys
import requests

url = sys.argv[1] if len(sys.argv) > 1 else ''

try:
    res = requests.get(url)
    if res.ok:
        print(res.text)
    else:
        res.raise_for_status()
except requests.exceptions.HTTPError as e:
    print("Error code:", e.response.status_code)
