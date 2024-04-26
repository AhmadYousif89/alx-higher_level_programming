#!/bin/bash
# script that takes in a URL, sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -o /dev/null -sIw "%{http_code}" "$1"
