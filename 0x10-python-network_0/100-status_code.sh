#!/bin/bash
#Create a curl requests with data in the header
curl -s -o /dev/null -w "%{http_code}" "$1"
