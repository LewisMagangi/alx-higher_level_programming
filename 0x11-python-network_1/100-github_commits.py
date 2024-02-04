#!/usr/bin/python3
"""  fetches github user repo commits  """
import requests
import sys

if __name__ == "__main__":
    response = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(sys.argv[2], sys.argv[1]))
    counter = 0
    for commit in sorted(response.json(), key=lambda c: c.get('commit')
                         .get('author').get('date'), reverse=True):
        print(commit.get('sha') + ": ", end="")
        print(commit.get('commit').get('author').get('name'))
        counter += 1
        if counter == 10:
            break