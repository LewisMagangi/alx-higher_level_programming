#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import sys
import requests

if __name__ == '__main__':

    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]
    
    response = requests.get(url, auth=(username, password))
    json_content = response.json()
    try:
        print(json_content['id'])
    except KeyError:
        print("None")
