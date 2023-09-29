#!/bin/bash
# This script sends a POST request to the specified URL with custom parameters and displays the body of the response
curl -s -X POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
