#!/bin/bash
# Perform a GET request to the specified URL while including a custom header variable.
curl -sH "X-School-User-Id: 98" "${1}"
