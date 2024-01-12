#!/usr/bin/python3
"""
a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import requests
import sys
import urllib.parse
import urllib.request

url = sys.argv[1]
email = sys.argv[2]

response = requests.post(url, data={'email': email})
print(response.text)
