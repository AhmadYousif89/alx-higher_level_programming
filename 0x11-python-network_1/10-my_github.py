#!/usr/bin/python3
"""
script that takes a GitHub username and password as arguments and uses
Basic Authentication with the GitHub API to display the user ID.
"""

if __name__ == "__main__":
    import sys
    import requests

    username = sys.argv[1]
    password = sys.argv[2] if len(sys.argv) > 2 else ''
    if not username or not password:
        exit(1)

    url = f'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    user_info = response.json()
    print(user_info.get('id'))
