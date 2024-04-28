#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL 
and displays the value of the X-Request-Id variable 
found in the header of the response.
"""

import sys
import urllib.request

url = sys.argv[1] if len(sys.argv) > 1 else ''

with urllib.request.urlopen(url) as response:
    req_id = response.getheader('X-Request-Id')
    print(req_id)
