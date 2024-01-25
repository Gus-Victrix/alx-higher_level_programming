#!/bin/bash
# Prints "You got me!" after querying 0.0.0.0:5000/catch_me
curl -s -w "You got me!"  0.0.0.0:5000/catch_me
