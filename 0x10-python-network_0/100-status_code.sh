#!/bin/bash
# Initiates a request to a specified URL as an argument and displays
# only the response status code without using a pipe.
awk 'NR==1{printf "%s", $2}' test7 $(curl -sI "$1" -o test7)
