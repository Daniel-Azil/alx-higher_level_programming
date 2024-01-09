#!/bin/bash
# Requests 0.0.0.0:5000/catch_me and sets a header variable with a PUT request, leading to the message "You got me!".
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
