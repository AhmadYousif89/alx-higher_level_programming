#!/bin/bash
# script that takes in a URL, sends a POST request to the URL with the following body:
## email: "test@gmail.com"
## subject: "I will always be here for PLD"

if [ "$#" -ne 1 ] ; then
    exit 1
fi

curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
