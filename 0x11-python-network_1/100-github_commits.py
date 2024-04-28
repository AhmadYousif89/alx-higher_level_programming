#!/usr/bin/python3
"""
script that lists the first 10 commits of a given Github repository
e.g repo: “rails” by the user: “rails”.
"""

if __name__ == "__main__":
    import sys
    import requests

    repo_name = sys.argv[1] if len(sys.argv) > 1 else ''
    author_name = sys.argv[2] if len(sys.argv) > 2 else ''
    if not repo_name or not author_name:
        exit(1)

    url = f'https://api.github.com/repos/{author_name}/{repo_name}/commits'
    response = requests.get(url)
    commits = response.json()
    first_10_commits = commits[:10]
    for commit in first_10_commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
