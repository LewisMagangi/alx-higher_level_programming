#!/bin/bash

# Check if an argument (URL) is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL from the first argument
url="$1"

# Use curl to send a GET request to the URL and capture the response
response=$(curl -s "$url")

# Display the size of the response body in bytes
response_size=$(echo -n "$response" | wc -c)
echo $response_size
