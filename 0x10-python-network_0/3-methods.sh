#!/usr/bin/env bash
# Displaying all HTTP methods that are acceptable.
if [ -z "$1" ] ; then
	exit
fi
curl -X OPTIONS "$1" -s
