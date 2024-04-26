#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

if [ ! "$1" ] ; then
    exit 1
fi

curl -so /dev/null -w "%{size_download}\n" "$1"
