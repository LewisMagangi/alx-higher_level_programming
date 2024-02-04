#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays
the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        print(response.text)
    except requests.exceptions.HTTPError as http_err:
        print(f"Error code: {response.status_code}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error code: {response.status_code}")
    except Exception as e:
        print(f"Error code: {response.status_code}")
