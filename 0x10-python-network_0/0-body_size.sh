#!/bin/bash
#This is a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.
echo -n (curl -s "$0" | wc -c
: '
  This is a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.

  The size must be displayed in bytes.
  You have to use curl.

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
'
