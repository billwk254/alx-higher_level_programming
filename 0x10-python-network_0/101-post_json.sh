#!/bin/bash
# This script sends a JSON POST request to a URL and displays the response body

curl -sX POST -H "Content-Type: application/json" --data @"$2" "$1"
