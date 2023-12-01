#!/usr/bin/env bash
# Displaying body of GET response
if [ -z "$1" ] ; then
	exit
fi
curl -H "X-School-User-Id=98" -X GET "$1"
