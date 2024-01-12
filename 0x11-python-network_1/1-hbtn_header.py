#!/usr/bin/python3
import urllib.request

url = "https://alx-intranet.hbtn.io/status"
request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    html_content = response.read()
    utf8_content = html_content.decode('utf-8')

    # Display the value of X-Request-Id if present
    x_request_id = response.getheader('X-Request-Id')
    if x_request_id:
        print(f"{x_request_id}")
