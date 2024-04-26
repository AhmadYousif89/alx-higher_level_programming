#!/bin/bash
# script that takes in a URL, and sends a POST request to that URL. 
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
