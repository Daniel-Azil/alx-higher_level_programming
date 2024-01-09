#!/bin/bash
# Initiates a JSON POST request to a specified URL using a given JSON file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
