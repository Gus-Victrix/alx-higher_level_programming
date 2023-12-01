#!/bin/bash
#Create a curl requests and display the Method Allowed
curl -X OPTIONS "$1" -si | grep "Allow:" | cut -d ' ' -f2-
