#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays 
the value of the variable X-Request-Id in the response header
"""

import sys
import requests

url = sys.argv[1] if len(sys.argv) > 1 else ''
email = sys.argv[2] if len(sys.argv) > 2 else ''

data = {"email": email}
res = requests.post(url, data)
print(res.text)
