#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests

if __name__ == '__main__':

    if len(sys.argv) > 1:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ""}

    url = 'http://0.0.0.0:5000/search_user'

    response = requests.post(url, data)

    try:
        json = response.json()
        if json == {}:
            print("No result")
        else:
            print("[{}] {}".format(json['id'], json['name']))

    except ValueError:
        print("Not a valid JSON")
