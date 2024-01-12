#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys

# Retrieve the URL from the command line argument
url = sys.argv[1]

# Create a Request object with the specified URL
request = urllib.request.Request(url)

# Use a with statement to open the URL and make the request
with urllib.request.urlopen(request) as response:
    # Display the value of X-Request-Id if present
    x_request_id = response.getheader('X-Request-Id')
    if x_request_id:
        print(f"{x_request_id}")
