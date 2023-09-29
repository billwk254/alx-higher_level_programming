#!/bin/bash
# This script takes a URL, sends a GET request, and displays the body of the response (200 status code only)
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")

if [ "$response" -eq 200 ]; then
    curl -s "$1"
fi
