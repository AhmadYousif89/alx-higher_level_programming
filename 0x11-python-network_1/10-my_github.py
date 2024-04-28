#!/usr/bin/python3
"""
script that takes a GitHub username and password as arguments and uses 
Basic Authentication with the GitHub API to display the user ID.
"""
import sys
import requests


username = sys.argv[1]
password = sys.argv[2]
url = f'https://api.github.com/users/{username}'
response = requests.get(url, auth=(username, password))

if response.ok:
    user_info = response.json()
    print(user_info['id'])
else:
    print("None")
