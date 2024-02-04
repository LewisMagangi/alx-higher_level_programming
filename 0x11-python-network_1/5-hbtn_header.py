#!/usr/bin/python3
"""
a Python script that takes in a URL,
sends a request to the URL and displays the
value of the variable X-Request-Id in the response header
"""
import requests
import sys

if __name__ == "__main__":

    # Use a with statement to open the URL and make the request
    url = sys.argv[1]
    response = requests.get(url)
    value = response.info()
    print(value['X-Request-Id'])
