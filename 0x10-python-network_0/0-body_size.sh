#!/bin/bash
# This script takes a URL, and displays size in bytes
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
