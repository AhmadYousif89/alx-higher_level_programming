#!/bin/bash
# script that takes in a URL, sends a DELETE request to the URL passed as the first argument and displays the body of the response

if [ "$#" -ne 1 ] ; then
    exit 1
fi

curl -sX DELETE "$1"
