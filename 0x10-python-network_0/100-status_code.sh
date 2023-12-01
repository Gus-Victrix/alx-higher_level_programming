#!/usr/bin/env bash
# Checking only status code of the response.
curl -s -w '%{http_code}\n' "$1" -o /dev/null
