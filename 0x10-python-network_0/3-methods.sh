#!/bin/bash
# Displaying all HTTP methods that are acceptable.
curl -X OPTIONS "$1" -s
