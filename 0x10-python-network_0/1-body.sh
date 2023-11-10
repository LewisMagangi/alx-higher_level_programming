#!/bin/bash
#This is a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
#echo -n " $curl -s -X GET "$1")"
curl -s -X GET "$1"
