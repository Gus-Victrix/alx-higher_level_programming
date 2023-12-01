#!/usr/bin/bash
# Showing size of http response to input socket
curl -s -w '%{size_download}\n' -o /dev/null "$1"
