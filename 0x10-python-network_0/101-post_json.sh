#!/bin/bash
# script that sends a JSON POST request to a URL passed as the first argument.

if [ "$#" -ne 2 ] || [ ! -f "$2" ] ; then
    exit 1
fi

URL="$1"
JSON_FILE="$2"

curl -sX POST "$URL"  -H "Content-Type: application/json" -d "@$JSON_FILE"
