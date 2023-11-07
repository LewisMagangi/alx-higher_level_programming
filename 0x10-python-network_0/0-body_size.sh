#!/bin/bash
#This is a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.
echo -n (curl -s "$0" | wc -c
