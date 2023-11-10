#!/bin/bash
#This is a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
[[ $(curl -s -w "%{http_code}" -o temp.txt "$1" && tail -n 1 temp.txt) -eq 200 ]] && cat temp.txt | head -n -1
