#!/bin/bash
#This is a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
echo -n "$(curl -X "$1")"
