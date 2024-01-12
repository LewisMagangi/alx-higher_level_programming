#!/usr/bin/python3
import urllib.request

url = "https://alx-intranet.hbtn.io/status"
request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    html_content = response.read()
    utf8_content = html_content.decode('utf-8')

    print("Body response:")
    print("\t- type:", type(html_content))
    print("\t- content:", html_content)
    print("\t- utf8 content:", utf8_content)
