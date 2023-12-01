#!/usr/bin/env bash
# Displaying body of Get response.
if [ -z "$1" ] ; then
	exit
fi
curl -s -o /dev/null -w '%{http_code}' "$1" | {
	read -r status

if [ "$status" -eq 200 ] ; then
	curl -s "$1"
fi
}
