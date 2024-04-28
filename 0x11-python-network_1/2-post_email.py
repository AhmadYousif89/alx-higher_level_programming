#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""

import sys
from urllib import request, parse

url = sys.argv[1] if len(sys.argv) > 1 else ''
email = sys.argv[2] if len(sys.argv) > 2 else ''
if not url or not email:
    exit(1)

data = parse.urlencode({"email": email}).encode('ascii')
req = request.Request(url, data)
with request.urlopen(req) as response:
    res = response.read().decode('utf-8')
    print(res)
