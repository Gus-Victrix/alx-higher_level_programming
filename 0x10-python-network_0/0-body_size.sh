#!/usr/bin/env bash
# Showing size of http response to input socket
if [ -z "$1" ] ; then
	echo "No url"
	exit
fi
curl -s -w '%{size_download}\n' -o /dev/null "$1"
