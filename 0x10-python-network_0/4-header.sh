#!/bin/bash
#This is a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
echo "$(curl -X GET -H "X-School-User-Id: 98" "$1")"
