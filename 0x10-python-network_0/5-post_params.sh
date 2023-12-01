#!/usr/bin/env bash
# Display response of POST to server.
if [ -z "$1" ] ; then
	exit
fi
email="test@gmail.com"
subject="I will always be here for PLD"
curl -s -X POST -d"email=$email&subject=$subject" "$1"
