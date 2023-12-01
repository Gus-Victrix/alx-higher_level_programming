#!/usr/bin/bash
# Displaying body of Get response.
curl -s -o /dev/null -w '%{http_code}' "$1" | { read -r status; [ "$status" -eq 200 ] && curl -s "$1"; }
