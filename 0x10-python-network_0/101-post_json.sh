#!/usr/bin/env bash
# POSTing json file contents
if [ -z "$1" ] || [ -z "$2" ];then
    echo "Usage: $0 <URL> <JSON_FILE>"
    exit
fi

url="$1"
json_file="$2"

if [ ! -f "$json_file" ]; then
    echo "Error: JSON file not found."
    exit
fi

curl -s -X POST -H "Content-Type: application/json" -d "@$json_file" "$url"
