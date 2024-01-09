#!/bin/bash
# Display all HTTP methods accepted by the server for the given URL.
curl -Is "$1" | grep "Allow:" | cut -d ":" -f 2 | cut -c 2- | rev | cut -c 2- | rev
