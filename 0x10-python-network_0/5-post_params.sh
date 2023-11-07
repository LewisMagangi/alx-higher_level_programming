#!/bin/bash
#This is a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
echo "$(curl -X POST -d 'ee+wialways+be+here+for+PLD' "$1")"
