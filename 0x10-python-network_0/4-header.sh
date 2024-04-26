#!/bin/bash
# script that takes in a URL, sends a GET request to the URL with a header variable X-School-User-Id and value 98

if [ "$#" -ne 1 ] ; then
    exit 1
fi

curl -sH "X-School-User-Id: 98" "$1"
