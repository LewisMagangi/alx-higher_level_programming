#!/bin/bash

# Check if an argument (URL) is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL from the first argument
url="$1"

# Use curl to send a HEAD request to retrieve the headers
headers=$(curl -I "$url" 2>/dev/null)

# Check if the request was successful (HTTP status code 200)
if [ $? -eq 0 ]; then
    # Extract the Content-Length header from the headers using grep and awk
    content_length=$(echo "$headers" | grep -i 'Content-Length:' | awk '{print $2}')
    if [ -n "$content_length" ]; then
	echo "Content-Length: $content_length bytes"
    else
	echo "Content-Length header not found in the response headers."
    fi
else
    echo "Request failed."
fi
