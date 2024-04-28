#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the body
of the response (decoded in utf-8).
"""

if __name__ == "__main__":
    import sys
    from urllib import request
    from urllib.error import HTTPError, URLError

    url = sys.argv[1] if len(sys.argv) > 1 else ''

    try:
        with request.urlopen(url) as response:
            res = response.read().decode('utf-8')
            print(res)
    except HTTPError as e:
        print('Error code:', e.code)
