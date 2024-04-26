#!/bin/bash
# script that takes in a URL, and displays all HTTP methods the server will accept.

if [ "$#" -ne 1 ] ; then
    exit 1
fi

curl -sI  "$1" | grep -i "Allow" | cut -d ' ' -f 2-
