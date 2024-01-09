#!/bin/bash
# Execute a script that sends a POST request and displays the response body.
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
