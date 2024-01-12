#!/usr/bin/python3
import urllib.request

url = "https://alx-intranet.hbtn.io/status"
request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    html_content = response.read()

print(html_content)
