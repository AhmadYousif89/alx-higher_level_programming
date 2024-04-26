#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response

if [ "$#" -ne 1 ] ; then
    exit 1
fi

curl -Ls "$1"
