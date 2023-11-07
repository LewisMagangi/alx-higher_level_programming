#!/bin/bash
#This is  a Bash script that takes in a URL and displays all HTTP methods the server will accept.
echo "$(curl -i -X OPTIONS "$url" -s)"
