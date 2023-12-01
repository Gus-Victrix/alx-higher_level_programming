#!/usr/bin/env bash
# Sending delete request to the input url
if [ -z "$1" ] ; then
	exit
fi
curl -X DELETE "$1" -s
