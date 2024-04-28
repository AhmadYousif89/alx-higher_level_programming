#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a query parameter.
"""
import sys
import requests

url = 'http://0.0.0.0:5000/search_user'
query = sys.argv[1] if len(sys.argv) > 1 else ''

try:
    res = requests.post(url, data={"q": query})
    data = res.json()
    if res.ok and data:
        print(f"[{data['id']}] {data['name']}")
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
