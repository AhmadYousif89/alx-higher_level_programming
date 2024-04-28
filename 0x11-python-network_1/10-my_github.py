#!/usr/bin/python3
"""
script that takes a GitHub username and password as arguments and uses 
Basic Authentication with the GitHub API to display the user ID.
"""
import requests
import sys


def get_user_id(username, password):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url, auth=(username, password))

    if response.ok:
        user_info = response.json()
        print(user_info['id'])
    else:
        print("None")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    get_user_id(username, password)
