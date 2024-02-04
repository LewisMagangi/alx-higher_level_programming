#!/usr/bin/python3
"""
Write a Python script that takes in a URL, 
sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""
import sys
import urllib.parse
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            html_bytes = response.read()
            html = html_bytes.decode("utf-8")
            print(html)
            
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
        
    except urllib.error.URLError as e:
        # Handle URL-related errors
        print(f"URLError: {e.reason}")
    except Exception as e:
        print(f"Error code: {e.code}")
