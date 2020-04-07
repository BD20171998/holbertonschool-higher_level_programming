#!/bin/bash
# Bash script that takes in a URL,displays all HTTP methods that can be accepted
curl -sIL "$1" | grep -i Allow | cut -d " " -f2-
